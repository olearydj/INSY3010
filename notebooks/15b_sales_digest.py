"""Generate a sales summary report for one region of the 5k-sales dataset.

Usage:
    python 15b_sales_digest.py <region>

Example:
    python 15b_sales_digest.py Asia
"""

import sqlite3
import sys
from pathlib import Path

import pandas as pd

DB_PATH = Path(__file__).parent / "data" / "5k-sales.db"


def list_regions():
    """Return the sorted list of distinct regions in the database."""
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT Region FROM sales ORDER BY Region")
        return [row[0] for row in cur.fetchall()]


def resolve_region(user_input, regions):
    """Return the canonical region name matching user_input (case-insensitive), or None."""
    target = user_input.strip().lower()
    for region in regions:
        if region.lower() == target:
            return region
    return None


def print_regions(regions, file=sys.stdout):
    """Print available regions, quoting names that contain spaces."""
    print("Available regions:", file=file)
    for region in regions:
        if " " in region:
            print(f'  "{region}"', file=file)
        else:
            print(f"  {region}", file=file)


def load_region(region):
    """Return all sales for a region as a DataFrame with a Revenue column."""
    with sqlite3.connect(DB_PATH) as con:
        df = pd.read_sql_query(
            "SELECT * FROM sales WHERE Region = ?",
            con,
            params=(region,),
        )
    df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
    return df


def top_countries(df, n=5):
    """Return top n countries by total units sold."""
    return (
        df.groupby("Country")["Units_Sold"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def top_items(df, n=5):
    """Return top n item types by total revenue."""
    return (
        df.groupby("Item_Type")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def print_report(region, df):
    """Print a formatted text report to stdout."""
    print(f"=== Sales Digest: {region} ===")
    print(f"Orders:        {len(df):,}")
    print(f"Total units:   {df['Units_Sold'].sum():,}")
    print(f"Total revenue: ${df['Revenue'].sum():,.2f}")
    print()

    print("Top 5 countries by units sold:")
    for country, units in top_countries(df).items():
        print(f"  {country:20s} {units:>12,}")
    print()

    print("Top 5 item types by revenue:")
    for item, revenue in top_items(df).round(2).items():
        print(f"  {item:20s} ${revenue:>15,.2f}")


def main():
    regions = list_regions()

    if len(sys.argv) != 2:
        print("Usage: python 15b_sales_digest.py <region>", file=sys.stderr)
        print(file=sys.stderr)
        print_regions(regions, file=sys.stderr)
        return 1

    region = resolve_region(sys.argv[1], regions)
    if region is None:
        print(f"Unknown region: {sys.argv[1]!r}", file=sys.stderr)
        print(file=sys.stderr)
        print_regions(regions, file=sys.stderr)
        return 1

    df = load_region(region)
    print_report(region, df)

    out_path = Path(__file__).parent / f"digest_{region.lower().replace(' ', '_')}.csv"
    df.to_csv(out_path, index=False)
    print(f"\nSaved {len(df)} rows to {out_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
