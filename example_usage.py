#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example usage of the TongHuaShun Stock Crawler
示例：如何使用同花顺股票爬虫
"""

from stock_crawler import TongHuaShunCrawler
import pandas as pd
import time


def example_single_stock():
    """Example: Collect data for a single stock"""
    print("=" * 60)
    print("Example 1: Single Stock Collection")
    print("示例1：单个股票数据采集")
    print("=" * 60)
    
    crawler = TongHuaShunCrawler()
    
    # Collect data for stock 002230
    stock_code = '002230'
    print(f"\nCollecting data for stock: {stock_code}")
    
    stock_data = crawler.get_stock_info(stock_code)
    
    # Export to Excel
    output_file = f'example_stock_{stock_code}.xlsx'
    crawler.export_to_excel(stock_data, output_file)
    print(f"Data saved to: {output_file}\n")


def example_multiple_stocks():
    """Example: Collect data for multiple stocks"""
    print("=" * 60)
    print("Example 2: Multiple Stocks Collection")
    print("示例2：多个股票数据采集")
    print("=" * 60)
    
    crawler = TongHuaShunCrawler()
    
    # List of stock codes to collect
    stock_codes = ['002230', '000001', '600000', '600519', '000858']
    
    all_data = []
    
    for i, code in enumerate(stock_codes, 1):
        print(f"\n[{i}/{len(stock_codes)}] Collecting data for stock: {code}")
        
        stock_data = crawler.get_stock_info(code)
        all_data.append(stock_data)
        
        # Add a small delay between requests to be polite
        if i < len(stock_codes):
            time.sleep(1)
    
    # Convert to DataFrame and export
    df = pd.DataFrame(all_data)
    output_file = 'example_multiple_stocks.xlsx'
    df.to_excel(output_file, index=False, engine='openpyxl')
    
    print(f"\nAll data saved to: {output_file}")
    print(f"Total stocks collected: {len(all_data)}\n")


def example_custom_fields():
    """Example: Collect data and display specific fields"""
    print("=" * 60)
    print("Example 3: Display Specific Fields")
    print("示例3：显示特定字段")
    print("=" * 60)
    
    crawler = TongHuaShunCrawler()
    
    stock_code = '002230'
    print(f"\nCollecting data for stock: {stock_code}")
    
    stock_data = crawler.get_stock_info(stock_code)
    
    # Display only key indicators
    key_indicators = [
        '股票代码',
        '现价',
        '量比',
        '换手率',
        '市盈(动)',
        'MA5',
        'MA10',
        'MA21',
        'MACD',
        'KDJ',
        'RSI'
    ]
    
    print("\nKey Indicators:")
    print("-" * 40)
    for indicator in key_indicators:
        value = stock_data.get(indicator, 'N/A')
        print(f"{indicator:15s}: {value}")
    print("-" * 40)


def main():
    """Run all examples"""
    print("\n")
    print("*" * 60)
    print("TongHuaShun Stock Crawler - Usage Examples")
    print("同花顺股票爬虫 - 使用示例")
    print("*" * 60)
    print("\n")
    
    # Run examples
    example_single_stock()
    print("\n")
    
    example_multiple_stocks()
    print("\n")
    
    example_custom_fields()
    print("\n")
    
    print("*" * 60)
    print("All examples completed!")
    print("所有示例完成！")
    print("*" * 60)


if __name__ == '__main__':
    main()
