import sys
from housing import pipeline
from housing.exception import HousingException
from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import Configuration


def main():

    try:
        # conf = Configuration()
        # print(conf.get_data_transformation_config())
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        raise HousingException(e,sys) from e

if __name__ == "__main__":
    main()