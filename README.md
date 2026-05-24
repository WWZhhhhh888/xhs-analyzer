# 小红书内容分析助手 📕

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/WWZhhhhh888/xhs-analyzer?style=social)](https://github.com/WWZhhhhh888/xhs-analyzer)

> 把你的小红书数据变成可复用的爆款公式

## ✨ 功能

| 功能 | 说明 | 状态 |
|------|------|------|
| 📊 互动率计算 | (点赞+评论+收藏)/观看 | ✅ |
| 📈 赞藏比分析 | 判断内容类型（情绪/干货） | ✅ |
| 💬 评论情感分析 | AI分析评论区情绪 | ✅ |
| ✍️ 标题优化 | AI评分+优化建议 | ✅ |
| 📉 历史趋势 | 记录每次分析 | ✅ |

## 📊 真实数据验证

基于本人3篇小红书笔记的真实数据：

| 指标 | 笔记1 | 笔记2 | 笔记3 |
|------|-------|-------|-------|
| 观看量 | 1.5w | 2.1w | 5.5k |
| 互动率 | 9.15% | 5.93% | 1.47% |
| 评论率 | 6.32% | 4.25% | 0.56% |
| 内容类型 | 情绪价值型 | 情绪价值型 | 情绪价值型 |

## 🔍 核心洞察

> 💡 **互动率的关键**：能让用户"想说两句"的内容，互动率是普通内容的 3-6 倍

> 💡 **高评论率的秘诀**：主动制造讨论点（提问、争议、分享经历）

> 💡 **优化方向**：增加干货型内容，提高收藏率

## 📝 爆款公式

### 公式1：技术 + 成果 + 开源

**标题**：大一搞定XXX，我做到了

**适合**：技术类账号

### 公式2：地域 + 争议 + 共鸣

**标题**：上海人对各自的高中有什么评价

**适合**：校园/生活类账号

## 🚀 快速开始

```bash
# 1. 克隆
git clone https://github.com/WWZhhhhh888/xhs-analyzer.git
cd xhs-analyzer

# 2. 安装依赖
pip install streamlit pandas plotly openai python-dotenv

# 3. 配置API Key
echo "DEEPSEEK_API_KEY=你的密钥" > .env

# 4. 运行
streamlit run app.py
