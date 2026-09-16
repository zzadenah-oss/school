import streamlit as st

# 페이지 설정 (넓은 화면 사용)
st.set_page_config(
    page_title="학교 문제 상황의 현상과 진단 - 구조도", layout="wide"
)

# 전체 배경 및 스타일 설정
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FBF9F1;
        color: #2C2C2C;
        font-family: 'Malgun Gothic', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #1A365D;
        margin-bottom: 25px;
        border-bottom: 2px solid #CBD5E1;
        padding-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 타이틀 출력
st.markdown(
    '<div class="main-title">학교 문제 상황에 어떻게 대응할까 (현상과 진단)</div>',
    unsafe_allow_html=True,
)


# 공통 카드 생성 함수 (좌우 흐름을 컬럼으로 구현)
def render_flow_row(title, left_desc, right_col1_title, right_col1_content, right_col2_title, right_col2_content, bottom_box_html="", bg_color="#F0F4F8", border_color="#3182CE"):
  with st.container():
    # 전체를 감싸는 시각적 박스
    st.markdown(f"""
        <div style="background-color: {bg_color}; border-left: 6px solid {border_color}; border: 1px solid #E2E8F0; border-left-width: 6px; border-radius: 8px; padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
        """, unsafe_allow_html=True)
    
    col1, col_arrow, col2 = st.columns([1.2, 0.2, 2.8])
    
    with col1:
      st.markdown(f"### {title}")
      st.markdown(left_desc)
      
    with col_arrow:
      st.markdown("<h2 style='text-align: center; color: #718096; margin-top: 20px;'>➔</h2>", unsafe_allow_html=True)
      
    with col2:
      sub_col1, sub_col2 = st.columns(2)
      with sub_col1:
        st.markdown(f"**{right_col1_title}**")
        st.markdown(right_col1_content)
      with sub_col2:
        st.markdown(f"**{right_col2_title}**")
        st.markdown(right_col2_content)
        
      if bottom_box_html:
        st.markdown("<hr style='margin: 10px 0; border:0; border-top:1px dashed #CBD5E1;'>", unsafe_allow_html=True)
        st.markdown(bottom_box_html, unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 1. 형식적인 교육활동
# ==========================================
render_flow_row(
    title="1. 형식적인 교육활동[cite: 3]",
    left_desc="• 교사의 노동에 비해 교육적 호자(효과)가 미미 또는 유명무실<br>• 행정적으로 잘하려 하지 않기[cite: 3]",
    right_col1_title="생기부 때문에 하는 것(들)[cite: 3]",
    right_col1_content="• 진로, 탐구, 멘토링, 독서 등 (주로) 학년부 중심의 교육활동<br>• 정규교과 수업 밖에서 이루어지는 교과/비교과 차원의 교육활동[cite: 3]",
    right_col2_title="해야 하니까 하는 것(들)[cite: 3]",
    right_col2_content="• 각종 예방교육, 사회정서교육, 민주시민교육 등<br>• *실제 필요성은 있으나 효과성이 없거나, 하는지 아무도 모름*[cite: 3]",
    bottom_box_html="<b>반쯤 죽은 노동[cite: 3]</b><br>• <b>불가능한 것 / 필요성 불분명한 것</b> ⇒ 걷어내기[cite: 3]<br>• <b>해야 하고 (제대로 기획하면) 할 수 있는 것</b> ⇒ 맥락화 (배움과 성장이라는 교육의 본질 위에서, 학교와 공부 이외의 다양한 기능과 역량이 빛나도록)[cite: 3]",
    bg_color="#F0F4F8",
    border_color="#3182CE"
)


# ==========================================
# 2. 교사의 피로와 무력감
# ==========================================
render_flow_row(
    title="2. 교사의 피로와 무력감[cite: 3]",
    left_desc="관계와 맥락은 없고 일만 남은 소모적 전쟁 상태[cite: 3]",
    right_col1_title="원인: <구조적 한계>[cite: 3]",
    right_col1_content="• 필요한 교육이 실제성 있게 이루어지지 않아 필연적 발생<br>• 개인화·전능화·탈정치화로 교사 개인의 과제로 전가됨<br>• *but, 개별 교사 차원에서 대응 불가능한 문제가 대부분*[cite: 3]",
    right_col2_title="접근 및 대응[cite: 3]",
    right_col2_content="• <b><전제>:</b> 개별 교사 차원의 문제를 개인 책임감에 의존하지 않음[cite: 3]<br>• <b><대응 ①>:</b> 시간표 내 일상적/정기적/안정적 대화 구조 확립<br>&nbsp;&nbsp;- *\"업무보다 수업, 수업보다 대화\"* (실무자 위주, 외롭지 않도록 부담 덜기)[cite: 3]<br>• <b><대응 ②>:</b> 교사가 교육활동 기획의 주체로 (자치, 실행자 결정권 최대화)[cite: 3]",
    bg_color="#FEFCBF",
    border_color="#DD6B20"
)


# ==========================================
# 3. 규범의 공백
# ==========================================
with st.container():
  st.markdown("""
        <div style="background-color: #FAF5FF; border-left: 6px solid #805AD5; border: 1px solid #E2E8F0; border-left-width: 6px; border-radius: 8px; padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
        """, unsafe_allow_html=True)
  
  col1, col_arrow, col2 = st.columns([1.2, 0.2, 2.8])
  with col1:
    st.markdown("### 3. 규범의 공백[cite: 3]")
    st.markdown("금지와 제한이 사라진 공백[cite: 3]")
  with col_arrow:
    st.markdown("<h2 style='text-align: center; color: #718096; margin-top: 10px;'>➔</h2>", unsafe_allow_html=True)
  with col2:
    st.markdown("**공적 대화와 동료관계 형성[cite: 3]**")
    st.markdown("• 함께 배우는 교사를 포함한 공적인 대화의 동료관계 형성 구조에서 규법을 논의[cite: 3]<br>• 기존 시민교육 방식의 실패 극복[cite: 3]")
    
  st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 최종 지향점: 교사의 성장
# ==========================================
st.markdown(
    """
    <div style="background-color: #FFF5F5; border: 2px solid #FEB2B2; border-radius: 8px; padding: 15px; margin-top: 25px; text-align: center;">
        <h3 style="color: #9B2C2C; margin-bottom: 10px;">🎯 최종 지향점: 교사의 성장[cite: 3]</h3>
    """,
    unsafe_allow_html=True,
)

col_g1, col_g2 = st.columns(2)
with col_g1:
  st.markdown("""
        <div style="background: #FFFFFF; padding: 12px; border-radius: 6px; border: 1px solid #FEB2B2; text-align: left;">
            ❌ <b>지양해야 할 구조</b><br>
            학생의 성상을 초점으로 두면 교사의 헌신을 요구하는 구조가 등장하기 쉬우나 <b>지속가능성 없음</b>[cite: 3]
        </div>
        """, unsafe_allow_html=True)
with col_g2:
  st.markdown("""
        <div style="background: #FFFFFF; padding: 12px; border-radius: 6px; border: 1px solid #C6F6D5; text-align: left;">
            ⭕ <b>바른 방향</b><br>
            어차피 교사의 성장은 <b>보통의 교사가 보통의 노력으로</b>, <b>학생의 배움과 성장을 바탕으로</b> 이루어짐[cite: 3]
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
