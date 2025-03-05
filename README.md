# S3 Bucket Object Counter

This Python script counts the number of objects in an S3-compatible object storage bucket. It supports both hardcoded credentials and command-line arguments for flexibility.

## Features
- Connects to an S3-compatible object storage.
- Counts the number of objects in a specified bucket.
- Supports command-line arguments for dynamic configuration.
- Uses `boto3` for AWS S3 API interactions.

## Prerequisites
- Python 3.x
- `boto3` and `botocore` libraries
- dotenv

### Install Dependencies
```sh
pip install boto3 botocore python-dotenv
```

Or alternatively usign uv:
```sh
uv init
uv sync
```

## Usage
You can run the script with default values or override them using command-line arguments.

### Run with Defaults
Modify the script to set your storage credentials and bucket name, then execute:
```sh
python count_objects.py
```

Or alternatively usign uv:
```sh
uv run count_objects.py
```

### Run with Command-line Arguments
You can override the default values with:
```sh
python count_objects.py -b <bucket-name> -a <api-url> -k <access-key> -s <secret-key>
```

### Command-line Arguments
| Argument  | Description |
|-----------|-------------|
| `-b`, `--bucket` | Name of the bucket (default: set in script) |
| `-a`, `--api-url` | S3-compatible storage URL (default: set in script) |
| `-k`, `--key` | Access key for authentication (default: set in script) |
| `-s`, `--secret` | Secret key for authentication (default: set in script) |

## Example
```sh
python count_objects.py -b mybucket -a https://s3.example.com -k myAccessKey -s mySecretKey
```

## License
This project is licensed under the MIT License.

