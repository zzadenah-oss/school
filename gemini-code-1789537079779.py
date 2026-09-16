import streamlit as st

# 페이지 설정 (넓은 화면 사용)
st.set_page_config(page_title="학교 문제 상황의 현상과 진단", layout="wide")

# 원본 노트의 시각적 감성(노트 패드 배경, 영역별 컬러 박스 등)을 구현하기 위한 CSS
st.markdown(
    """
    <style>
    /* 전체 앱 배경색 (노트 패드 느낌의 따뜻한 크림/아이보리 톤) */
    .stApp {
        background-color: #FBF9F1;
        color: #2C2C2C;
        font-family: 'Malgun Gothic', sans-serif;
    }
    
    /* 타이틀 스타일 */
    .main-title {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #1A365D;
        margin-bottom: 25px;
        border-bottom: 2px solid #CBD5E1;
        padding-bottom: 10px;
    }

    /* 공통 카드 박스 스타일 (원본의 손글씨 영역 느낌) */
    .note-box {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }

    /* 영역별 색상 강조 테두리 및 배경 */
    .box-formal {
        border-left: 5px solid #3182CE; /* 파란색 계열: 형식적 교육활동 */
        background-color: #F0F4F8;
    }
    .box-fatigue {
        border-left: 5px solid #DD6B20; /* 주황색 계열: 교사의 피로와 무력감 */
        background-color: #FEFCBF;
    }
    .box-norm {
        border-left: 5px solid #805AD5; /* 보라색 계열: 규범의 공백 */
        background-color: #FAF5FF;
    }
    .box-solution {
        border-left: 5px solid #38A169; /* 초록색 계열: 대응 및 맥락화 */
        background-color: #F0FFF4;
    }
    .box-growth {
        border-left: 5px solid #E53E3E; /* 붉은색 계열: 교사의 성장 */
        background-color: #FFF5F5;
    }

    /* 텍스트 세부 스타일 */
    h4 {
        margin-top: 0;
        color: #2D3748;
    }
    .tag {
        display: inline-block;
        background-color: #E2E8F0;
        color: #4A5568;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
        margin-right: 5px;
    }
    .arrow {
        text-align: center;
        font-size: 20px;
        color: #718096;
        margin: 5px 0;
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

# 레이아웃 구성 (2단 컬럼 구조로 원본의 좌우 흐름 반영)
col_left, col_right = st.columns([1.1, 0.9])

with col_left:
  st.markdown("### 📌 현상 영역 (3가지 축)", unsafe_allow_html=True)

  # 1. 형식적인 교육활동
  st.markdown(
      """
        <div class="note-box box-formal">
            <h4>1. 형식적인 교육활동</h4>
            <ul>
                <li><b>생기부 때문에 하는 것(들)</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;• 진로, 탐구, 멘토링, 독서 등 (주로) 학년부 중심의 교육활동<br>
                &nbsp;&nbsp;&nbsp;&nbsp;• 정규교과 수업 밖에서 이루어지는 교과/비교과 차원의 교육활동</li>
                <li><b>해야 하니까 하는 것(들)</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;• 각종 예방교육, 사회정서교육, 민주시민교육 등<br>
                &nbsp;&nbsp;&nbsp;&nbsp;• <i>실제 필요성은 있으나 효과성이 없거나, 하는지 아무도 모름</i></li>
            </ul>
            <p>👉 <b>현상:</b> 교사의 노동에 비해 교육적 호자(효과)가 미미 또는 유명무실 / 행정적으로 잘하려 하지 않기</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # 1번에 대한 대응 (걷어내기 및 맥락화)
  st.markdown(
      """
        <div class="note-box box-solution" style="margin-left: 20px;">
            <h4>↳ [형식적 교육활동 대응]</h4>
            <p><span class="tag" style="background:#FED7D7; color:#9B2C2C;">불가능한 것 / 필요성 불분명</span> ⇒ <b>걷어내기</b> (반쯤 죽은 노동)</p>
            <p><span class="tag" style="background:#C6F6D5; color:#22543D;">해야 하고 제대로 기획할 수 있는 것</span> ⇒ <b>맥락화</b></p>
            <p style="font-size: 13px; color: #555; margin-left: 15px;">
            • 배움과 성장이라는 교육의 본질 위에서<br>
            • 학교와 공부 이외의 다양한 기능과 역량이 빛나도록
            </p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # 2. 교사의 피로와 무력감
  st.markdown(
      """
        <div class="note-box box-fatigue">
            <h4>2. 교사의 피로와 무력감</h4>
            <p><b>원인 - <구조적 한계></b><br>
            • 필요한 교육이 실제성 있게 이루어지지 않았기 때문에 필연적으로 드러나는 문제<br>
            • 개인화·전능화·탈정치화: 교사 개인의 과제로 전가됨.<br>
            &nbsp;&nbsp;<i>but, 실제로는 개별 교사 차원에서 대응 불가능한 문제가 대부분</i></p>
            <hr style="border:0; border-top:1px dashed #CBD5E1; margin:10px 0;">
            <p><b>접근 및 대응</b><br>
            • <b><전제>:</b> 개별 교사 차원에서 대응할 수 없는 문제를 교사 개인의 책임감에 의존하지 않아야 함<br>
            • <b><대응>:</b><br>
            &nbsp;&nbsp;① <b>시간표 내에서 일상적/정기적/안정적인 대화의 구조 확립</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <i>"업무보다 수업, 수업보다 대화"</i><br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 행정은 실무자에게, 일하는 사람이 외롭지 않도록 부담 덜기<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 교사-학생 간, 교사-교사 간 대화 구조<br>
            &nbsp;&nbsp;② <b>교사가 교육활동 기획의 주체로 자리매김 (자치)</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 실제 실행하는 사람의 권한/결정권을 최대화
            </p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # 3. 규범의 공백
  st.markdown(
      """
        <div class="note-box box-norm">
            <h4>3. 규범의 공백</h4>
            <p>• 금지와 제한이 사라진 공백<br>
            • 함께 배우는 교사를 포함한 공적인 대화의 동료관계 형성 구조에서 규법을 논의<br>
            • 기존 시민교육 방식의 실패 극복</p>
        </div>
        """,
      unsafe_allow_html=True,
  )


with col_right:
  st.markdown("### 🎯 최종 지향점", unsafe_allow_html=True)

  st.markdown(
      """
        <div class="note-box box-growth">
            <h3 style="color: #9B2C2C; text-align: center; margin-bottom: 10px;">교사의 성장</h3>
            <hr style="border:0; border-top:1px solid #FEB2B2; margin:10px 0;">
            <p>❌ <b>지양해야 할 구조:</b><br>
            학생의 성상을 초점으로 두면 교사의 헌신을 요구하는 구조가 등장하기 쉬우나 <b>지속가능성 없음</b></p>
            <br>
            <p>⭕ <b>바른 방향:</b><br>
            어차피 교사의 성장은 <b>보통의 교사가 보통의 노력으로</b>, <b>학생의 배움과 성장을 바탕으로</b> 이루어짐</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div style="background-color: #EDF2F7; padding: 15px; border-radius: 8px; border: 1px dashed #CBD5E1; text-align: center; margin-top: 20px;">
            <p style="margin: 0; font-size: 13px; color: #4A5568;">
            💡 <b>팁:</b> 이 웹앱은 원본 노트의 구조적 배치를 웹 화면으로 옮긴 것입니다.<br>
            필요에 따라 코드를 수정하여 내용을 덧붙이거나 활용할 수 있습니다.
            </p>
        </div>
        """,
      unsafe_allow_html=True,
  )