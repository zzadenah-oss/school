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


# ==========================================
# 1. 형식적인 교육활동 (요청 사항 반영 재배치)
# ==========================================
with st.container():
  st.markdown(
      """
        <div style="background-color: #F0F4F8; border-left: 6px solid #3182CE; border: 1px solid #E2E8F0; border-left-width: 6px; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
        """,
      unsafe_allow_html=True,
  )

  col1, arrow1, col2, arrow2, col3, arrow3, col4 = st.columns(
      [1.1, 0.1, 1.3, 0.1, 1.0, 0.1, 1.6]
  )

  with col1:
    st.markdown("### 1. 형식적인 교육활동[cite: 3]")
    st.markdown("- 행정적으로 잘하려 하지 않기[cite: 3]")

  with arrow1:
    st.markdown(
        "<h2 style='text-align: center; color: #718096; margin-top:"
        " 40px;'>➔</h2>",
        unsafe_allow_html=True,
    )

  with col2:
    st.markdown("**생기부 때문에 하는 것(들)[cite: 3]**")
    st.markdown("- 교사의 노동에 비해 교육적 효과가 미미 또는 유명무실[cite: 3]")
    st.markdown(
        "- 학년부 중심의 교육활동 및 교과수업 밖에서 이루어지는 교육활동(진로,"
        " 탐구, 멘토링, 독서, 봉사 등)[cite: 3]"
    )

    st.markdown(
        "<hr style='margin: 10px 0; border:0; border-top:1px dashed #CBD5E1;'>",
        unsafe_allow_html=True,
    )

    st.markdown("**해야 하니까 하는 것(들)[cite: 3]**")
    st.markdown(
        "- 실제 필요성은 있음 but 효과성이 없거나 또는 왜 하는지 아무도 모름"
        "[cite: 3]"
    )
    st.markdown("- 각종 예방교육, 사회정서교육, 민주시민교육 등[cite: 3]")

  with arrow2:
    st.markdown(
        "<h2 style='text-align: center; color: #718096; margin-top:"
        " 40px;'>➔</h2>",
        unsafe_allow_html=True,
    )

  with col3:
    st.markdown("### 반쯤 죽은 노동[cite: 3]")

  with arrow3:
    st.markdown(
        "<h2 style='text-align: center; color: #718096; margin-top:"
        " 40px;'>➔</h2>",
        unsafe_allow_html=True,
    )

  with col4:
    st.markdown(
        "- **불가능한 것 / 필요성이 불분명한 것**<br>&nbsp;&nbsp;⇒"
        " **걷어내기**[cite: 3]",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<hr style='margin: 10px 0; border:0; border-top:1px dashed #CBD5E1;'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "- **해야 하고 (제대로 기획하면) 할 수 있는 것**<br>&nbsp;&nbsp;⇒"
        " **맥락화**<br><span style='font-size:12px; color:#555;'>(배움과 성장이라는"
        " 교육의 본질 위에서, 학교와 공부 이외의 다양한 기능과 역량이"
        " 빛나도록)</span>[cite: 3]",
        unsafe_allow_html=True,
    )

  st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 2. 교사의 피로와 무력감
# ==========================================
with st.container():
  st.markdown(
      """
        <div style="background-color: #FEFCBF; border-left: 6px solid #DD6B20; border: 1px solid #E2E8F0; border-left-width: 6px; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
        """,
      unsafe_allow_html=True,
  )

  col1, col_arrow, col2 = st.columns([1.2, 0.2, 2.8])

  with col1:
    st.markdown("### 2. 교사의 피로와 무력감[cite: 3]")
    st.markdown("- 관계와 맥락은 없고 일만 남은 소모적 전쟁 상태[cite: 3]")

  with col_arrow:
    st.markdown(
        "<h2 style='text-align: center; color: #718096; margin-top:"
        " 20px;'>➔</h2>",
        unsafe_allow_html=True,
    )

  with col2:
    sub1, sub2 = st.columns(2)
    with sub1:
      st.markdown("**원인: <구조적 한계>[cite: 3]**")
      st.markdown(
          "- 필요한 교육이 실제성 있게 이루어져 있지 않아 필연적 발생[cite: 3]"
      )
      st.markdown(
          "- 개인화·전능화·탈정치화로 교사 개인의 과제로 전가됨[cite: 3]"
      )
      st.markdown(
          "- *but, 개별 교사 차원에서 대응 불가능한 문제가 대부분*[cite: 3]"
      )
    with sub2:
      st.markdown("**접근 및 대응[cite: 3]**")
      st.markdown(
          "- **<전제>:** 개별 교사 차원의 문제를 개인 책임감에 의존하지 않음"
          "[cite: 3]"
      )
      st.markdown(
          "- **<대응 ①>:** 시간표 내 일상적/정기적/안정적 대화 구조 확립\n"
          "  - *\"업무보다 수업, 수업보다 대화\"* (실무자 위주, 외롭지 않도록"
          " 부담 덜기)[cite: 3]"
      )
      st.markdown(
          "- **<대응 ②>:** 교사가 교육활동 기획의 주체로 (자치, 실행자 결정권"
          " 최대화)[cite: 3]"
      )

  st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 3. 규범의 공백
# ==========================================
with st.container():
  st.markdown(
      """
        <div style="background-color: #FAF5FF; border-left: 6px solid #805AD5; border: 1px solid #E2E8F0; border-left-width: 6px; border-radius: 8px; padding: 20px; margin-bottom: 20px;">
        """,
      unsafe_allow_html=True,
  )

  col1, col_arrow, col2 = st.columns([1.2, 0.2, 2.8])

  with col1:
    st.markdown("### 3. 규범의 공백[cite: 3]")
    st.markdown("- 금지와 제한이 사라진 공백[cite: 3]")

  with col_arrow:
    st.markdown(
        "<h2 style='text-align: center; color: #718096; margin-top:"
        " 10px;'>➔</h2>",
        unsafe_allow_html=True,
    )

  with col2:
    st.markdown("**공적 대화와 동료관계 형성[cite: 3]**")
    st.markdown(
        "- 함께 배우는 교사를 포함한 공적인 대화의 동료관계 형성 구조에서 규법을"
        " 논의[cite: 3]"
    )
    st.markdown("- 기존 시민교육 방식의 실패 극복[cite: 3]")

  st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 최종 지향점: 교사의 성장
# ==========================================
st.markdown(
    """
    <div style="background-color: #FFF5F5; border: 2px solid #FEB2B2; border-radius: 8px; padding: 20px; margin-top: 25px; text-align: center;">
        <h3 style="color: #9B2C2C; margin-bottom: 15px;">🎯 최종 지향점: 교사의 성장[cite: 3]</h3>
    """,
    unsafe_allow_html=True,
)

col_g1, col_g2 = st.columns(2)
with col_g1:
  st.markdown(
      """
        <div style="background: #FFFFFF; padding: 15px; border-radius: 6px; border: 1px solid #FEB2B2; text-align: left;">
            ❌ <b>지양해야 할 구조</b>[cite: 3]<br>
            학생의 성상을 초점으로 두면 교사의 헌신을 요구하는 구조가 등장하기 쉬우나 <b>지속가능성 없음</b>[cite: 3]
        </div>
        """,
      unsafe_allow_html=True,
  )
with col_g2:
  st.markdown(
      """
        <div style="background: #FFFFFF; padding: 15px; border-radius: 6px; border: 1px solid #C6F6D5; text-align: left;">
            ⭕ <b>바른 방향</b>[cite: 3]<br>
            어차피 교사의 성장은 <b>보통의 교사가 보통의 노력으로</b>, <b>학생의 배움과 성장을 바탕으로</b> 이루어짐[cite: 3]
        </div>
        """,
      unsafe_allow_html=True,
  )

st.markdown("</div>", unsafe_allow_html=True)
