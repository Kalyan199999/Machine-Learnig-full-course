import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging 

from src.utils import save_object


import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

@dataclass
class DataTranformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    
    '''
    This method is responsible for data transformation
    '''
    def __init__(self):
        self.data_transformation_config=DataTranformationConfig()

    def get_data_transformer_object(self):
        try:
           numerical_cols =  ['reading score', 'writing score']
           
           categorical_cols = ['gender','race/ethnicity','parental level of education','lunch','test preparation course']
           num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="median")),
                ('scaler', StandardScaler(with_mean=False))   # ✅ FIX
            ])

           logging.info(f"Numerical columns Scaling is  compleded! ")
           cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="most_frequent")),
                ('onehot', OneHotEncoder(handle_unknown='ignore')),
                ('scaler', StandardScaler(with_mean=False))   # ✅ keep this False too
            ])

           logging.info(f"Categorical columns encoding compleded! ")

           preprocesser = ColumnTransformer(
               transformers=[
                   ("numerical features" , num_pipeline , numerical_cols),
                   ("categorical features" , cat_pipeline , categorical_cols)
                   
               ],
               remainder="passthrough"
           )

           logging.info(f"Data preprocessing is completed! ")

           return preprocesser
           
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data Transformation initiated")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_object = self.get_data_transformer_object()

            target_column_name = 'math score'

           
            
            numerical_cols =  ['reading score', 'writing score']

            categorical_cols = ['gender','race/ethnicity','parental level of education','lunch','test preparation course']

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            
            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            
            logging.info("Applying preprocessing object on training dataframe and testing dataframe")

            input_feature_train_arr =  preprocessing_object.fit_transform(input_feature_train_df)

            input_feature_test_arr = preprocessing_object.transform(input_feature_test_df)

            target_feature_train_df = train_df[target_column_name]

            target_feature_test_df = test_df[target_column_name]

            train_arr = np.c_[
                input_feature_train_arr , np.array(target_feature_train_df)
            ]

            test_arr = np.c_[input_feature_test_arr , np.array(target_feature_test_df)]

            logging.info('Saving Preprocessing object.')

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_object
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

            
        except Exception as e:
            raise CustomException(e,sys)