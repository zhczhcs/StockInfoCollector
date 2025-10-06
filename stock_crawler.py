#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stock Information Collector for TongHuaShun (同花顺)
Collects various stock indicators and exports to Excel
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Dict, Optional
import time
import json


class TongHuaShunCrawler:
    """TongHuaShun stock information crawler"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        
    def get_stock_info(self, stock_code: str) -> Dict[str, any]:
        """
        Get comprehensive stock information for a given stock code
        
        Args:
            stock_code: Stock code (e.g., '002230')
            
        Returns:
            Dictionary containing all stock indicators
        """
        stock_data = {
            '股票代码': stock_code,
            '现价': None,
            '量比': None,
            '换手率': None,
            '市盈(动)': None,
            'BOLLUP': None,
            'PER': None,
            'KDJ': None,
            '主力吸筹': None,
            'BBI': None,
            'MACD': None,
            'RSI': None,
            'RSI买入': None,
            '主力拉升': None,
            '尾盘资金流入(亿)': None,
            '收盘获利%': None,
            '平均成本': None,
            '筹码集中度': None,
            'OBV': None,
            '股东人数少': None,
            '基金持%': None,
            '诊股分': None,
            '机构目标价': None,
            '主力控盘': None,
            '估值': None,
            'MA5': None,
            'MA10': None,
            'MA21': None,
        }
        
        try:
            # Get basic stock info from TongHuaShun
            basic_info = self._get_basic_info(stock_code)
            stock_data.update(basic_info)
            
            # Get technical indicators
            tech_indicators = self._get_technical_indicators(stock_code)
            stock_data.update(tech_indicators)
            
            # Get fund flow data
            fund_flow = self._get_fund_flow(stock_code)
            stock_data.update(fund_flow)
            
            # Get chip distribution data
            chip_data = self._get_chip_distribution(stock_code)
            stock_data.update(chip_data)
            
            # Get fundamental data
            fundamental_data = self._get_fundamental_data(stock_code)
            stock_data.update(fundamental_data)
            
        except Exception as e:
            print(f"Error collecting data for {stock_code}: {str(e)}")
            
        return stock_data
    
    def _get_basic_info(self, stock_code: str) -> Dict[str, any]:
        """Get basic stock information (price, volume, etc.)"""
        data = {}
        
        try:
            # TongHuaShun stock page URL
            url = f'http://stockpage.10jqka.com.cn/{stock_code}/'
            response = self.session.get(url, timeout=10)
            response.encoding = 'gbk'
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                
                # Extract current price (现价)
                price_elem = soup.select_one('.price')
                if price_elem:
                    data['现价'] = price_elem.text.strip()
                
                # Extract other basic indicators from the page
                # These selectors need to be adjusted based on actual page structure
                indicators = soup.select('.company_details dl dd')
                
                for indicator in indicators:
                    text = indicator.text.strip()
                    if '量比：' in text:
                        data['量比'] = text.split('：')[1] if '：' in text else text.split(':')[1]
                    elif '换手：' in text or '换手率：' in text:
                        value = text.split('：')[1] if '：' in text else text.split(':')[1]
                        data['换手率'] = value.replace('%', '')
                    elif '市盈(动)：' in text or '市盈：' in text:
                        value = text.split('：')[1] if '：' in text else text.split(':')[1]
                        data['市盈(动)'] = value
                        
        except Exception as e:
            print(f"Error getting basic info: {str(e)}")
            
        return data
    
    def _get_technical_indicators(self, stock_code: str) -> Dict[str, any]:
        """Get technical indicators (MACD, KDJ, RSI, MA, etc.)"""
        data = {}
        
        try:
            # TongHuaShun technical analysis API
            url = f'http://d.10jqka.com.cn/v6/line/{stock_code}/01/last.js'
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                # Parse technical indicator data
                # This is a simplified example - actual implementation needs proper parsing
                content = response.text
                
                # Extract MA indicators
                if 'ma5' in content.lower():
                    data['MA5'] = 'N/A'  # Placeholder - needs proper extraction
                if 'ma10' in content.lower():
                    data['MA10'] = 'N/A'
                if 'ma21' in content.lower() or 'ma20' in content.lower():
                    data['MA21'] = 'N/A'
                
                # Extract other technical indicators
                data['MACD'] = 'N/A'  # Placeholder
                data['KDJ'] = 'N/A'
                data['RSI'] = 'N/A'
                data['BBI'] = 'N/A'
                data['BOLLUP'] = 'N/A'
                data['OBV'] = 'N/A'
                
        except Exception as e:
            print(f"Error getting technical indicators: {str(e)}")
            
        return data
    
    def _get_fund_flow(self, stock_code: str) -> Dict[str, any]:
        """Get fund flow data (主力资金流入流出等)"""
        data = {}
        
        try:
            # TongHuaShun fund flow page
            url = f'http://stockpage.10jqka.com.cn/{stock_code}/funds/'
            response = self.session.get(url, timeout=10)
            response.encoding = 'gbk'
            
            if response.status_code == 200:
                # Parse fund flow data
                data['主力吸筹'] = 'N/A'  # Placeholder
                data['主力拉升'] = 'N/A'
                data['尾盘资金流入(亿)'] = 'N/A'
                data['主力控盘'] = 'N/A'
                
        except Exception as e:
            print(f"Error getting fund flow: {str(e)}")
            
        return data
    
    def _get_chip_distribution(self, stock_code: str) -> Dict[str, any]:
        """Get chip distribution data (筹码分布、获利比例等)"""
        data = {}
        
        try:
            # TongHuaShun chip distribution page
            url = f'http://stockpage.10jqka.com.cn/{stock_code}/chip/'
            response = self.session.get(url, timeout=10)
            response.encoding = 'gbk'
            
            if response.status_code == 200:
                # Parse chip distribution data
                data['收盘获利%'] = 'N/A'  # Placeholder
                data['平均成本'] = 'N/A'
                data['筹码集中度'] = 'N/A'
                
        except Exception as e:
            print(f"Error getting chip distribution: {str(e)}")
            
        return data
    
    def _get_fundamental_data(self, stock_code: str) -> Dict[str, any]:
        """Get fundamental data (估值、股东人数、基金持股等)"""
        data = {}
        
        try:
            # TongHuaShun fundamental page
            url = f'http://basic.10jqka.com.cn/{stock_code}/'
            response = self.session.get(url, timeout=10)
            response.encoding = 'gbk'
            
            if response.status_code == 200:
                # Parse fundamental data
                data['PER'] = 'N/A'  # Placeholder
                data['RSI买入'] = 'N/A'
                data['股东人数少'] = 'N/A'
                data['基金持%'] = 'N/A'
                data['诊股分'] = 'N/A'
                data['机构目标价'] = 'N/A'
                data['估值'] = 'N/A'
                
        except Exception as e:
            print(f"Error getting fundamental data: {str(e)}")
            
        return data
    
    def export_to_excel(self, stock_data: Dict[str, any], filename: str = 'stock_info.xlsx'):
        """
        Export stock data to Excel file
        
        Args:
            stock_data: Dictionary containing stock information
            filename: Output Excel filename
        """
        try:
            # Convert to DataFrame
            df = pd.DataFrame([stock_data])
            
            # Reorder columns to match requirement
            column_order = [
                '股票代码',
                '现价',
                '量比',
                '换手率',
                '市盈(动)',
                'BOLLUP',
                'PER',
                'KDJ',
                '主力吸筹',
                'BBI',
                'MACD',
                'RSI',
                'RSI买入',
                '主力拉升',
                '尾盘资金流入(亿)',
                '收盘获利%',
                '平均成本',
                '筹码集中度',
                'OBV',
                '股东人数少',
                '基金持%',
                '诊股分',
                '机构目标价',
                '主力控盘',
                '估值',
                'MA5',
                'MA10',
                'MA21',
            ]
            
            # Reorder dataframe columns
            df = df[column_order]
            
            # Export to Excel
            df.to_excel(filename, index=False, engine='openpyxl')
            print(f"Data exported successfully to {filename}")
            
        except Exception as e:
            print(f"Error exporting to Excel: {str(e)}")
            

def main():
    """Main function to run the crawler"""
    print("=" * 60)
    print("TongHuaShun Stock Information Collector")
    print("同花顺股票信息采集器")
    print("=" * 60)
    
    # Initialize crawler
    crawler = TongHuaShunCrawler()
    
    # Test with stock code 002230
    stock_code = '002230'
    print(f"\nCollecting data for stock: {stock_code}")
    print("-" * 60)
    
    # Get stock information
    stock_data = crawler.get_stock_info(stock_code)
    
    # Print collected data
    print("\nCollected Data:")
    for key, value in stock_data.items():
        print(f"{key}: {value}")
    
    # Export to Excel
    print("\n" + "-" * 60)
    output_file = f'stock_{stock_code}_info.xlsx'
    crawler.export_to_excel(stock_data, output_file)
    
    print("\n" + "=" * 60)
    print("Data collection completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()
