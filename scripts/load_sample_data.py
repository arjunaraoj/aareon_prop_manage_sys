import pandas as pd
import os
from pathlib import Path

def load_sample_data():
    """Load sample CSV data into the system"""
    data_dir = Path("./data/raw")
    
    # Load all CSV files
    csv_files = {
        "properties": pd.read_csv(data_dir / "properties.csv"),
        "tenants": pd.read_csv(data_dir / "tenants.csv"),
        "maintenance_requests": pd.read_csv(data_dir / "maintenance_requests.csv"),
        "customer_inquiries": pd.read_csv(data_dir / "customer_inquiries.csv")
    }
    
    # Basic statistics
    for name, df in csv_files.items():
        print(f"\n{name.upper()} Data:")
        print(f"Records: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        print(f"Sample:\n{df.head(2)}")
    
    return csv_files

if __name__ == "__main__":
    load_sample_data()