def house_reco(door, sun, grass, fence):
    score = 0
    result = ""
    if door < 1:
        result += "고립 위축 "
        score += 1
    elif door == 1:
        result += "개방적 "
    else:
        result += "은둔적 "
        score += 1

    if sun == 1:
        result += "의존적 "
        score += 1
    elif sun > 1:
        result += "애정욕구 "
        score += 1
    else:
        result += "자립적 "

    if grass > 5:
        result += "안정감부족 "
        score += 1
    else:
        result += "안정적 "
    if fence > 1:
        score += 1
        result += "방어적 "
    else:
        result += "개방적 "

    if score == 4:
        result += """
        /다른 사람이 자기 자신의 삶, 세계 안에 들어오는 것에 대해서 불안감 혹은 저항감을
        느끼며 자신만의 세계에 고립되고 위축되어 있음을 의미한다. 사회적 접근 가능성이 과다함을 의미하여
        사회적인 인정이나 수용에 지나치게 의존적이거나 타인과의 친밀한 관계에 지나친 비중을 두거나
        과도하게 예민해 한다.
        """
    elif score == 3:
        result += """/다른 사람들과 관계를 맺고 싶은 욕구도 있지만 다른 한편으로는 이에 대한 거부감, 두려움,
                불편감 등의 양가 감정을 느끼고 있을 가능성이 있다."""
    elif score == 2:
        result += """/강력한 부모와 같은 자기 대상 존재를 갈망하고 있음을 암시할 수 있다.
        아동의 경우 발달적으로 미성숙하므로 이러한 양상이 나타나는 것이 일반적이나 태양을 지나치게 강조해서 그릴 경우는 강한 애정욕구 및
        이에 대한 좌절감을 암시할 수 있다."""
    elif score == 1:
        result += "/자기를 돌보거나 지배하는 강력한 부모와 같은 자기 대상을 경험하고 있음을 의미할 수 있다."
    else:
        result += "/정상적이며 문제되는 부분이 없어보인다."
    return result, score

def personReco(ear, nose, mouth, arm, eye):
    result = ""
    score = 0
    if ear == 1:
        score += 1
        result += "회피적태도 "
    elif ear == 0:
        score += 1
        result += "두려움"
    else:
        result += "자립적"

    if nose == 0:
        score += 1
        result += "위축감 "
    elif nose == 1:
        esult += "안정적"

    if mouth < 1:
        score += 1
        result += "의사소통거부"

    if arm != 2:
        score += 1
        result += "죄의식 "

    if eye == 1:
        score += 1
        result += "회피적태도 "
    elif eye != 2:
        score += 1
        result += "소극적 "

    if score == 5:
        result += "/때때로 동성연애자에게 나타나며, 비평에 극도로 민감한 신경증 환자 성에대한 무언가 갈등이 있으며 남성적인 것을 거부하며 거세불안이 있고 동성애 경향이 있을 가능성이 있다."
    elif score == 4:
        result += "/죄의식, 극단적 우울증, 일반적인 무력감, 환경에 대한 불만, 강한 철회 경향 등을 나타난다. 사회적 교류에 대해 접근 회피의 양가감정, 사회적 불안 등을 반영 열등감, 부적절감, 낮은 자존감, 불안, 수줍음과 위축, 과도한 자기 억제, 사회적 철수 경향, 낮은 자아강도, 의존적 경향등이 나타난다."
    elif score == 3:
        result += "/대인관계에 대한 두려움, 위축감, 회피적 태도를 나타낸다. 상당한 심리 신체적 천식의 상태이며 우울 상태의 가능성이 높고 타인들과 의사소통하는 것을 원하지 않는다. 공격적, 행동화 경향, 과장적 경향, 조증상태, 과도한 자신감, 자아팽창, 부적절감을 보상 또는 억압 방어 등이 나타난다."
    elif score == 2:
        result += "/애정과 관심에 대한 욕구가 강하거나 대인관계에서 지나치게 예민함을 보이며 사회적 교류에 대해 접근 회피의 양가감정, 사회적 불안 등이 나타난다."
    elif score == 1:
        result += "/애정 욕구의 강한 거부, 심한 죄의식, 천식 환자, 우울 감정을 갖고 있다."
    else:
        result += "/정상적이며 문제되는 부분이 없어보인다."

    return result