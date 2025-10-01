import os

from pyiceberg.catalog import load_catalog
# from auth0_token import get_client_credentials_token

def main():
    cat = load_catalog(
        "uc",
        **{
            "type": "rest",
            "uri": os.environ["UC_ICEBERG_URI"],
            "warehouse": os.environ.get("UC_WAREHOUSE", "unity"),
            # "token": token,
            # "header.X-Iceberg-Access-Delegation",
        },
    )
    print(cat.list_tables("default"))
    tab = cat.load_table(("default", "marksheet_uniform"))
    print(tab.scan().to_arrow())


if __name__ == "__main__":
    main()
