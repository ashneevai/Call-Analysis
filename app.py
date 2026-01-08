"""Streamlit Web UI for Verizon Customer Call Classification System."""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from tools.classification_tools import (
    classify_call_category,
    analyze_call_transcript,
    extract_customer_info,
    generate_classification_report
)

# Page configuration
st.set_page_config(
    page_title="Verizon Call Classifier",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for call history
if 'call_history' not in st.session_state:
    st.session_state.call_history = []

# ==================== HEADER ====================
st.markdown("# 📞 ABC Telecom Customer Call Classifier")
st.markdown("### AI-Powered Call Classification & Analysis System")
st.markdown("---")

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    # Info section
    st.markdown("### 📊 About")
    st.info("""
    This system classifies ABC Telecom customer support calls into 8 categories:
    - **Billing** - Invoices, payments, pricing
    - **Technical Support** - Network, connectivity issues
    - **Account Management** - Plan changes, account info
    - **Customer Service** - General inquiries, complaints
    - **Retention** - Cancellation prevention, offers
    - **Sales** - Upgrades, new services
    - **Refund** - Refunds, credits, compensation
    - **Fraud** - Security concerns, unauthorized activity
    """)
    
    st.markdown("### 🎯 Classification Method")
    method = st.radio(
        "Select Classification Method:",
        ["Keyword-Based (Fast)", "AI-Powered (Slow)"],
        help="Keyword-based is instant, AI-powered requires API key"
    )
    
    st.markdown("### 📈 Call History")
    show_history = st.checkbox("Show Call History", value=False)

# ==================== MAIN CONTENT ====================

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📥 Classify Call", "📊 Analysis", "📋 Batch Process", "📚 Sample Calls"])

# ==================== TAB 1: CLASSIFY CALL ====================
with tab1:
    st.markdown("## Single Call Classification")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Input area
        transcript = st.text_area(
            "Paste Customer Call Transcript:",
            placeholder="""Example:
Customer: Hi, I've been having internet issues all week.
Agent: I'm sorry to hear that. Let me help troubleshoot.
Customer: The connection keeps dropping.
Agent: Let me escalate this to technical support.""",
            height=300,
            key="transcript_input"
        )
    
    with col2:
        st.markdown("### 📋 Quick Tips")
        st.markdown("""
        - **Paste** a full call transcript
        - **Click** "Classify Call"
        - **Review** detailed analysis
        - **Export** results
        """)
    
    # Classify button
    if st.button("🔍 Classify Call", use_container_width=True, type="primary"):
        if transcript.strip():
            with st.spinner("🔄 Analyzing call..."):
                try:
                    # Analyze the transcript
                    analysis = analyze_call_transcript(transcript)
                    customer_info = extract_customer_info(transcript)
                    classification = classify_call_category(transcript, analysis)
                    
                    # Store in session state
                    st.session_state.call_history.append({
                        'transcript': transcript,
                        'classification': classification,
                        'analysis': analysis,
                        'customer_info': customer_info
                    })
                    
                    # Display results
                    st.success("✅ Classification Complete!")
                    
                    # Main classification card
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric(
                            "Primary Category",
                            classification['primary_category'].upper(),
                            f"{classification['confidence_score']}% confident"
                        )
                    
                    with col2:
                        st.metric(
                            "Sentiment",
                            analysis['sentiment'],
                            analysis['urgency_level'] + " Urgency"
                        )
                    
                    with col3:
                        st.metric(
                            "Duration Estimate",
                            analysis['duration_estimate'],
                            len(transcript.split()) + " words"
                        )
                    
                    st.markdown("---")
                    
                    # Detailed Results
                    col1, col2 = st.columns([1, 1])
                    
                    with col1:
                        st.markdown("### 📊 Classification Details")
                        st.markdown(f"""
                        **Primary Category:** {classification['primary_category'].upper()}
                        
                        **Description:** {classification['category_description']}
                        
                        **Confidence Score:** {classification['confidence_score']}%
                        
                        **Recommendation:** {classification['recommendation']}
                        """)
                    
                    with col2:
                        st.markdown("### 📝 Analysis Summary")
                        st.markdown(f"""
                        **Sentiment:** {analysis['sentiment']}
                        
                        **Urgency:** {analysis['urgency_level']}
                        
                        **Duration:** {analysis['duration_estimate']}
                        
                        **Topics:** {', '.join(analysis['key_topics'])}
                        """)
                    
                    st.markdown("---")
                    
                    # Customer Information
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("### 📱 Services Mentioned")
                        if customer_info['mentioned_services']:
                            for service in customer_info['mentioned_services']:
                                st.write(f"• {service.title()}")
                        else:
                            st.write("None identified")
                    
                    with col2:
                        st.markdown("### ⚠️ Issues Reported")
                        if customer_info['issues_reported']:
                            for issue in customer_info['issues_reported']:
                                st.write(f"• {issue.title()}")
                        else:
                            st.write("None reported")
                    
                    with col3:
                        st.markdown("### 🎯 Customer Requests")
                        if customer_info['requests']:
                            for request in customer_info['requests']:
                                st.write(f"• {request.title()}")
                        else:
                            st.write("No specific requests")
                    
                    st.markdown("---")
                    
                    # Category Confidence Chart
                    st.markdown("### 📊 Category Confidence Scores")
                    
                    # Prepare data for chart
                    categories = list(classification['all_scores'].keys())
                    scores = list(classification['all_scores'].values())
                    
                    # Create bar chart
                    fig = go.Figure(data=[
                        go.Bar(
                            x=categories,
                            y=scores,
                            marker_color=['#1f77b4' if cat == classification['primary_category'] else '#d3d3d3' 
                                        for cat in categories]
                        )
                    ])
                    fig.update_layout(
                        title="Confidence Scores by Category",
                        xaxis_title="Category",
                        yaxis_title="Score",
                        height=400,
                        showlegend=False
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    st.markdown("---")
                    
                    # Sentiment Indicators
                    if customer_info['sentiment_markers']:
                        st.markdown("### 💭 Sentiment Indicators")
                        for marker in customer_info['sentiment_markers']:
                            st.info(marker)
                    
                    # Full Report
                    with st.expander("📄 Full Classification Report"):
                        report = generate_classification_report(transcript)
                        st.text(report)
                    
                    # Export options
                    st.markdown("---")
                    st.markdown("### 💾 Export Options")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        report = generate_classification_report(transcript)
                        st.download_button(
                            label="📥 Download Report (TXT)",
                            data=report,
                            file_name="classification_report.txt",
                            mime="text/plain"
                        )
                    
                    with col2:
                        csv_data = f"""Category,Confidence,Sentiment,Urgency,Duration
{classification['primary_category']},{classification['confidence_score']},{analysis['sentiment']},{analysis['urgency_level']},{analysis['duration_estimate']}"""
                        st.download_button(
                            label="📊 Download CSV",
                            data=csv_data,
                            file_name="classification_data.csv",
                            mime="text/csv"
                        )
                    
                    with col3:
                        import json
                        json_data = json.dumps({
                            'classification': classification,
                            'analysis': analysis,
                            'customer_info': {k: v for k, v in customer_info.items() if k != 'sentiment_markers'}
                        }, indent=2)
                        st.download_button(
                            label="📋 Download JSON",
                            data=json_data,
                            file_name="classification_data.json",
                            mime="application/json"
                        )
                
                except Exception as e:
                    st.error(f"❌ Error processing call: {str(e)}")
        else:
            st.warning("⚠️ Please enter a call transcript first!")

# ==================== TAB 2: ANALYSIS ====================
with tab2:
    st.markdown("## Historical Analysis")
    
    if st.session_state.call_history:
        st.success(f"✅ Processed {len(st.session_state.call_history)} calls")
        
        # Summary statistics
        col1, col2, col3, col4 = st.columns(4)
        
        categories_list = [call['classification']['primary_category'] for call in st.session_state.call_history]
        
        with col1:
            st.metric("Total Calls", len(st.session_state.call_history))
        
        with col2:
            avg_confidence = sum([call['classification']['confidence_score'] for call in st.session_state.call_history]) / len(st.session_state.call_history)
            st.metric("Avg Confidence", f"{avg_confidence:.1f}%")
        
        with col3:
            st.metric("Unique Categories", len(set(categories_list)))
        
        with col4:
            sentiments = [call['analysis']['sentiment'] for call in st.session_state.call_history]
            st.metric("Most Common Sentiment", max(set(sentiments), key=sentiments.count))
        
        st.markdown("---")
        
        # Category distribution
        st.markdown("### 📊 Category Distribution")
        category_counts = pd.Series(categories_list).value_counts()
        
        fig = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title="Distribution of Call Categories"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Call history table
        st.markdown("### 📋 Call History")
        history_data = []
        for i, call in enumerate(st.session_state.call_history, 1):
            history_data.append({
                'Call #': i,
                'Category': call['classification']['primary_category'].upper(),
                'Confidence': f"{call['classification']['confidence_score']}%",
                'Sentiment': call['analysis']['sentiment'],
                'Urgency': call['analysis']['urgency_level']
            })
        
        df = pd.DataFrame(history_data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("📭 No calls classified yet. Start by classifying a call in the first tab!")

# ==================== TAB 3: BATCH PROCESS ====================
with tab3:
    st.markdown("## Batch Process Multiple Calls")
    
    st.markdown("""
    Paste multiple call transcripts separated by "---" divider
    """)
    
    batch_text = st.text_area(
        "Paste Multiple Transcripts (separated by ---):",
        height=400,
        placeholder="""Call 1 transcript here...

---

Call 2 transcript here...

---

Call 3 transcript here..."""
    )
    
    if st.button("⚡ Process Batch", use_container_width=True, type="primary"):
        if batch_text.strip():
            # Split by ---
            calls = [call.strip() for call in batch_text.split("---") if call.strip()]
            
            if calls:
                progress_bar = st.progress(0)
                results_list = []
                
                for i, transcript in enumerate(calls):
                    try:
                        analysis = analyze_call_transcript(transcript)
                        classification = classify_call_category(transcript, analysis)
                        
                        results_list.append({
                            'Call #': i + 1,
                            'Category': classification['primary_category'].upper(),
                            'Confidence': f"{classification['confidence_score']}%",
                            'Sentiment': analysis['sentiment'],
                            'Urgency': analysis['urgency_level']
                        })
                        
                        progress_bar.progress((i + 1) / len(calls))
                    except Exception as e:
                        st.error(f"Error processing call {i + 1}: {str(e)}")
                
                if results_list:
                    st.success(f"✅ Successfully processed {len(results_list)} calls!")
                    
                    # Display results
                    df = pd.DataFrame(results_list)
                    st.dataframe(df, use_container_width=True)
                    
                    # Category summary
                    st.markdown("---")
                    st.markdown("### 📊 Summary")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        category_counts = pd.Series([r['Category'] for r in results_list]).value_counts()
                        fig = px.bar(
                            x=category_counts.index,
                            y=category_counts.values,
                            title="Category Distribution",
                            labels={'x': 'Category', 'y': 'Count'}
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    with col2:
                        sentiment_counts = pd.Series([r['Sentiment'] for r in results_list]).value_counts()
                        fig = px.pie(
                            values=sentiment_counts.values,
                            names=sentiment_counts.index,
                            title="Sentiment Distribution"
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    # Download batch results
                    st.markdown("---")
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Batch Results (CSV)",
                        data=csv,
                        file_name="batch_results.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
            else:
                st.warning("⚠️ No transcripts found. Make sure they're separated by ---")
        else:
            st.warning("⚠️ Please enter at least one call transcript!")

# ==================== TAB 4: SAMPLE CALLS ====================
with tab4:
    st.markdown("## Sample Customer Calls")
    
    samples = [
        {
            "name": "Technical Support",
            "category": "🔧 Technical Support",
            "transcript": """Customer: Hi, my internet has been down for 2 days!
Agent: Oh no, let me check on that right away.
Customer: This is urgent - I work from home.
Agent: Let me escalate this immediately to our technical team."""
        },
        {
            "name": "Billing Issue",
            "category": "💳 Billing",
            "transcript": """Customer: I was charged twice last month!
Agent: That's not right. Let me look into your account.
Customer: This is the second time. I want a refund.
Agent: I sincerely apologize. I'll process that immediately."""
        },
        {
            "name": "Retention",
            "category": "🎯 Retention",
            "transcript": """Customer: I want to cancel my service.
Agent: I'm sorry to hear that. What's the reason?
Customer: Your prices are too high.
Agent: Let me see what special offers we can provide."""
        },
        {
            "name": "Account Update",
            "category": "👤 Account Management",
            "transcript": """Customer: I need to update my address.
Agent: Sure, I can help with that.
Customer: I've moved to a new place.
Agent: Perfect, I'll update your information right away."""
        },
        {
            "name": "Sales/Upgrade",
            "category": "📈 Sales",
            "transcript": """Customer: I'd like faster internet.
Agent: Great choice! We have plans for that.
Customer: What are the speeds?
Agent: We offer up to 940 Mbps!"""
        },
    ]
    
    for i, sample in enumerate(samples):
        with st.expander(f"{sample['category']} - {sample['name']}"):
            st.markdown("**Sample Transcript:**")
            st.text(sample['transcript'])
            
            if st.button(f"Classify this sample", key=f"sample_{i}"):
                with st.spinner("Classifying..."):
                    analysis = analyze_call_transcript(sample['transcript'])
                    classification = classify_call_category(sample['transcript'], analysis)
                    
                    st.success("✅ Classified!")
                    st.metric("Category", classification['primary_category'].upper(), f"{classification['confidence_score']}% confident")
                    st.info(classification['recommendation'])

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>🤖 <strong>Verizon Customer Call Classification System</strong> | Powered by AI 🚀</p>
    <p style="font-size: 0.8em; color: gray;">Version 1.0 | January 2026</p>
</div>
""", unsafe_allow_html=True)
