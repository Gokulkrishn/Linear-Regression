from housing import pipeline
from housing.exception import HousingException
from housing.pipeline.pipeline import Pipeline


def main():
    try:
        pipeline = Pipeline()

        pipeline.run_pipeline()
    except Exception as e:
        raise HousingException(e,sys) from e

if __name__ == "__main__":
    main()