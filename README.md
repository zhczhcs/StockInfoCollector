# StockInfoCollector

股票信息采集器 - 同花顺数据爬虫

## 项目简介

这是一个用于采集同花顺（TongHuaShun）网站股票信息的爬虫工具。可以自动获取股票的各项技术指标、资金流向、筹码分布等数据，并导出到Excel文件。

## 功能特点

- 自动采集股票各项指标数据
- 支持导出Excel格式
- 易于扩展和维护的模块化设计

## 采集的数据指标

本工具采集以下股票指标：

### 基本信息
- 现价
- 量比
- 换手率
- 市盈(动)

### 技术指标
- BOLLUP (布林线上轨)
- PER
- KDJ
- BBI (多空指数)
- MACD
- RSI
- RSI买入
- OBV (能量潮)
- MA5 (5日均线)
- MA10 (10日均线)
- MA21 (21日均线)

### 资金流向
- 主力吸筹
- 主力拉升
- 尾盘资金流入(亿)
- 主力控盘

### 筹码分布
- 收盘获利%
- 平均成本
- 筹码集中度

### 基本面数据
- 股东人数少
- 基金持%
- 诊股分
- 机构目标价
- 估值

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
python stock_crawler.py
```

默认会采集股票代码 002230 的数据，并导出到 `stock_002230_info.xlsx` 文件。

### 在代码中使用

```python
from stock_crawler import TongHuaShunCrawler

# 创建爬虫实例
crawler = TongHuaShunCrawler()

# 获取股票信息
stock_code = '002230'
stock_data = crawler.get_stock_info(stock_code)

# 导出到Excel
crawler.export_to_excel(stock_data, f'stock_{stock_code}_info.xlsx')
```

### 采集多只股票

```python
from stock_crawler import TongHuaShunCrawler
import pandas as pd

crawler = TongHuaShunCrawler()

# 股票代码列表
stock_codes = ['002230', '000001', '600000']

# 采集所有股票数据
all_data = []
for code in stock_codes:
    print(f"Collecting data for {code}...")
    stock_data = crawler.get_stock_info(code)
    all_data.append(stock_data)

# 导出到一个Excel文件
df = pd.DataFrame(all_data)
df.to_excel('all_stocks_info.xlsx', index=False)
```

## 项目结构

```
StockInfoCollector/
├── README.md              # 项目说明文档
├── requirements.txt       # Python依赖包列表
├── stock_crawler.py       # 主程序文件
└── .gitignore            # Git忽略文件配置
```

## 技术架构

### 核心类：TongHuaShunCrawler

主要方法：
- `get_stock_info(stock_code)`: 获取指定股票的所有信息
- `export_to_excel(stock_data, filename)`: 导出数据到Excel

内部方法：
- `_get_basic_info()`: 获取基本信息（价格、量比等）
- `_get_technical_indicators()`: 获取技术指标（MACD、KDJ等）
- `_get_fund_flow()`: 获取资金流向数据
- `_get_chip_distribution()`: 获取筹码分布数据
- `_get_fundamental_data()`: 获取基本面数据

## 依赖库

- requests: HTTP请求
- beautifulsoup4: HTML解析
- lxml: XML/HTML解析器
- openpyxl: Excel文件操作
- pandas: 数据处理

## 注意事项

1. 本工具仅供学习和研究使用
2. 请遵守目标网站的robots.txt协议和使用条款
3. 建议在请求之间添加适当的延迟，避免对服务器造成过大压力
4. 网站页面结构可能会变化，需要相应调整选择器

## 扩展开发

### 添加新的数据指标

在 `TongHuaShunCrawler` 类中添加新的方法：

```python
def _get_new_indicator(self, stock_code: str) -> Dict[str, any]:
    """Get new indicator data"""
    data = {}
    # Your implementation here
    return data
```

然后在 `get_stock_info()` 方法中调用：

```python
new_data = self._get_new_indicator(stock_code)
stock_data.update(new_data)
```

## 测试

默认使用股票代码 002230 (科大讯飞) 进行测试。

## 许可证

本项目仅供学习和研究使用。

## 贡献

欢迎提交 Issue 和 Pull Request！