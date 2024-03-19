# StockMarketEfficiency
Streamlining MicroServered Pipeline with SQS-Powered Data Flow

The project centers around developing a REST API that fetches stocks data from the "rapidapi" website After we hit the API link every 1 sec with the Python script and send the data to AWS SQS Once 10 records accumulate in the SQS queue, a separate AWS Lambda function named "Processor" is triggered to process this data. The processed data, containing information exclusively about stock name, price, high , low, then inserted into a DynamoDB No-SQL database.
