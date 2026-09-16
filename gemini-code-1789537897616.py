import streamlit as st

# 페이지 설정 (넓은 화면 사용)
st.set_page_config(
    page_title="학교 문제 상황의 현상과 진단", layout="wide"
)

# 커스텀 CSS 스타일 적용 (원 노트의 감성과 좌우 배치 디자인)
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
    .note-container {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }
    .box-formal { border-left: 6px solid #3182CE; background-color: #F0F4F8; }
    .box-fatigue { border-left: 6px solid #DD6B20; background-color: #FEFCBF; }
    .box-norm { border-left: 6px solid #805AD5; background-color: #FAF5FF; }
    .box-growth { border-left: 6px solid #E53E3E; background-color: #FFF5F5; }
    
    h3, h4 { color: #2D3748; margin-top: 0; }
    .sub-item {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 6px;
        padding: 10px 15px;
        margin-bottom: 10px;
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

# ==========================================
# [현상 1] 형식적인 교육활동
# ==========================================
st.markdown("### 1. 형식적인 교육활동", unsafe_allow_html=True)
with st.container():
  st.markdown(
      '<div class="note-container box-formal">', unsafe_allow_html=True
  )

  c1, c2 = st.columns([1, 1.3])
  with c1:
    st.markdown("#### 📌 현상 핵심")
    st.markdown(
        "• 교사의 노동에 비해 교육적 효과가 미미 또는"
        " 유명무실<br>• 행정적으로 잘하려 하지 않기",
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        """
        <div class="sub-item">
            <b>생기부 때문에 하는 것(들)</b><br>
            • 진로, 탐구, 멘토링, 독서 등 (주로) 학년부 중심의 교육활동<br>
            • 정규교과 수업 밖에서 이루어지는 교과/비교과 차원의 교육활동
        </div>
        <div class="sub-item">
            <b>해야 하니까 하는 것(들)</b><br>
            • 각종 예방교육, 사회정서교육, 민주시민교육 등<br>
            • <i>실제 필요성은 있으나 효과성이 없거나, 하는지 아무도 모름</i>
        </div>
        """,
        unsafe_allow_html=True,
    )

  # 형식적인 교육활동에 대한 대응 (걷어내기 및 맥락화)
  st.markdown(
      """
        <hr style="border:0; border-top:1px dashed #BEE3F8; margin: 15px 0;">
        <div style="background-color: #EBF8FF; padding: 12px; border-radius: 6px;">
            <b>↳ [대응 방안] 걷어내기 및 맥락화</b><br>
            • <b>불가능한 것 / 필요성 불분명한 것</b> ⇒ 걷어내기 (반쯤 죽은 노동)<br>
            • <b>해야 하고 제대로 기획할 수 있는 것</b> ⇒ 맥락화 (배움과 성장이라는 교육의 본질 위에서, 학교와 공부 이외의 다양한 기능·역량이 빛나도록)
        </div>
        """,
      unsafe_allow_html=True,
  )
  st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# [현상 2] 교사의 피로와 무력감
# ==========================================
st.markdown("### 2. 교사의 피로와 무력감", unsafe_allow_html=True)
with st.container():
  st.markdown(
      '<div class="note-container box-fatigue">', unsafe_allow_html=True
  )

  c1, c2 = st.columns([1, 1.3])
  with c1:
    st.markdown("#### 📌 원인 및 전제")
    st.markdown(
        "• <b><구조적 한계>:</b> 필요한 교육이 실제성 있게 이루어지지"
        " 않았기 때문에 필연적으로 드러나는 문제<br>•"
        " <b>개인화·전능화·탈정치화:</b> 교사 개인의 과제로 전가됨<br>&nbsp;&nbsp;<i>but,"
        " 실제로는 개별 교사 차원에서 대응 불가능한 문제가 대부분</i><br>•"
        " <b><전제>:</b> 개별 교사 차원에서 대응할 수 없는 문제를 교사 개인의"
        " 책임감에 의존하지 않아야 함",
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        """
        <div class="sub-item">
            <b>대응 방안 ①: 대화의 구조 확립</b><br>
            • 시간표 내에서 일상적/정기적/안정적인 대화 구조 확립<br>
            • <i>"업무보다 수업, 수업보다 대화"</i><br>
            • 행정은 실무자에게, 일하는 사람이 외롭지 않도록 부담 덜기 (교사-학생 간, 교사-교사 간)
        </div>
        <div class="sub-item">
            <b>대응 방안 ②: 기획의 주체로 자리매김 (자치)</b><br>
            • 교사가 교육활동 기획의 주체로 활동<br>
            • 실제 실행하는 사람의 권한과 결정권을 최대화
        </div>
        """,
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# [현상 3] 규범의 공백
# ==========================================
st.markdown("### 3. 규범의 공백", unsafe_allow_html=True)
with st.container():
  st.markdown('<div class="note-container box-norm">', unsafe_allow_html=True)

  c1, c2 = st.columns([1, 1.3])
  with c1:
    st.markdown("#### 📌 현상 및 문제점")
    st.markdown(
        "• 금지와 제한이 사라진 공백 상태<br>• 기존의 시민교육 방식이 실패하는"
        " 원인 제공",
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        """
        <div class="sub-item">
            <b>공적 대화와 규범 논의 구조</b><br>
            • 함께 배우는 교사를 포함한 공적인 대화의 동료관계 형성 구조 마련<br>
            • 해당 구조 속에서 규법을 새롭게 논의
        </div>
        """,
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# [최종 지향점] 교사의 성장
# ==========================================
st.markdown("### 🎯 최종 지향점", unsafe_allow_html=True)
with st.container():
  st.markdown(
      '<div class="note-container box-growth" style="text-align: center;">',
      unsafe_allow_html=True,
  )
  st.markdown("<h3 style='color: #9B2C2C;'>교사의 성장</h3>", unsafe_allow_html=True)
  st.markdown(
      """
        <div style="display: flex; justify-content: space-around; text-align: left; margin-top: 15px;">
            <div style="width: 45%; background: #FFF5F5; padding: 12px; border-radius: 6px; border: 1px solid #FEB2B2;">
                ❌ <b>지양해야 할 구조</b><br>
                학생의 성상을 초점으로 두면 교사의 헌신을 요구하는 구조가 등장하기 쉬우나 <b>지속가능성 없음</b>
            </div>
            <div style="width: 45%; background: #F0FFF4; padding: 12px; border-radius: 6px; border: 1px solid #C6F6D5;">
                ⭕ <b>바른 방향 (지향점)</b><br>
                어차피 교사의 성장은 <b>보통의 교사가 보통의 노력으로</b>, <b>학생의 배움과 성장을 바탕으로</b> 이루어짐
            </div>
        </div>
        """,
      unsafe_allow_html=True,
  )
  st.markdown("</div>", unsafe_allow_html=True)
