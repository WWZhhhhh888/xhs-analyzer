# 简化版 app.py（无 AI）
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

st.set_page_config(page_title="小红书内容分析助手", layout="wide")
st.title("📕 小红书内容分析助手")

with st.sidebar:
    st.header("📝 笔记数据输入")
    note_title = st.text_input("笔记标题")
    views = st.number_input("观看量", min_value=0, step=100)
    likes = st.number_input("点赞数", min_value=0, step=10)
    comments = st.number_input("评论数", min_value=0, step=5)
    saves = st.number_input("收藏数", min_value=0, step=10)
    analyze_btn = st.button("🚀 开始分析", type="primary")

if analyze_btn:
    if not note_title or views == 0:
        st.warning("请填写笔记标题和观看量")
        st.stop()
    
    st.header("📊 基础数据分析")
    
    col1, col2, col3 = st.columns(3)
    
    engagement = (likes + comments + saves) / views if views > 0 else 0
    col1.metric("互动率", f"{engagement:.2%}")
    
    if saves > 0:
        like_save_ratio = likes / saves
        col2.metric("赞藏比", f"{like_save_ratio:.2f}")
    else:
        col2.metric("赞藏比", "无收藏")
    
    comment_rate = comments / views if views > 0 else 0
    col3.metric("评论率", f"{comment_rate:.2%}")
    
    st.info("""
    **小红书行业基准**：
    - 优秀互动率：5-10%
    - 优秀评论率：0.5-1%
    - 赞藏比 > 1：情绪价值内容
    - 赞藏比 < 1：干货价值内容
    """)
    
    os.makedirs("analysis_history", exist_ok=True)
    record = pd.DataFrame([{
        "时间": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "标题": note_title,
        "观看量": views,
        "互动率": engagement
    }])
    csv_path = "analysis_history/records.csv"
    if os.path.exists(csv_path):
        existing = pd.read_csv(csv_path)
        updated = pd.concat([existing, record], ignore_index=True)
        updated.to_csv(csv_path, index=False)
    else:
        record.to_csv(csv_path, index=False)
    
    st.success("✅ 分析完成！")