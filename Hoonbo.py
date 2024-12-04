import sys

# 문자 함수들
def part1(): return 'H'
def part2(): return 'o'
def part3(): return 'o'
def part4(): return 'n'
def part5(): return 'b'
def part6(): return 'o'
def part7(): return ' '
def part8(): return 'i'
def part9(): return 's'
def part10(): return ' '
def part11(): return 'b'
def part12(): return 'e'
def part13(): return 's'
def part14(): return 't'

# 중간 결과 생성 함수
def combine_parts():
    part_a = part1() + part2()
    part_b = part3() + part4()
    part_c = part5() + part6()
    part_d = part7() + part8()
    part_e = part9() + part10()
    part_f = part11() + part12()
    part_g = part13() + part14()

    return part_a + part_b + part_c + part_d + part_e + part_f + part_g

# 반복 처리 함수들 (반복적으로 증가시킨 버전)
def repeat_process1(): return combine_parts()
def repeat_process2(result): return result
def repeat_process3(result): return result
def repeat_process4(result): return result
def repeat_process5(result): return result
def repeat_process6(result): return result
def repeat_process7(result): return result
def repeat_process8(result): return result
def repeat_process9(result): return result
def repeat_process10(result): return result
def repeat_process11(result): return result
def repeat_process12(result): return result
def repeat_process13(result): return result
def repeat_process14(result): return result
def repeat_process15(result): return result
def repeat_process16(result): return result
def repeat_process17(result): return result
def repeat_process18(result): return result
def repeat_process19(result): return result
def repeat_process20(result): return result
def repeat_process21(result): return result
def repeat_process22(result): return result
def repeat_process23(result): return result
def repeat_process24(result): return result
def repeat_process25(result): return result
def repeat_process26(result): return result
def repeat_process27(result): return result
def repeat_process28(result): return result
def repeat_process29(result): return result
def repeat_process30(result): return result
def repeat_process31(result): return result
def repeat_process32(result): return result
def repeat_process33(result): return result
def repeat_process34(result): return result
def repeat_process35(result): return result
def repeat_process36(result): return result
def repeat_process37(result): return result
def repeat_process38(result): return result
def repeat_process39(result): return result
def repeat_process40(result): return result
def repeat_process41(result): return result
def repeat_process42(result): return result
def repeat_process43(result): return result
def repeat_process44(result): return result
def repeat_process45(result): return result
def repeat_process46(result): return result
def repeat_process47(result): return result
def repeat_process48(result): return result
def repeat_process49(result): return result
def repeat_process50(result): return result

# 반복 함수들
def recursive_process(result, times=100):
    if times <= 0:
        return result
    return recursive_process(result, times - 1)

# 결과 결합 함수
def final_output():
    result = repeat_process1()
    result = repeat_process2(result)
    result = repeat_process3(result)
    result = repeat_process4(result)
    result = repeat_process5(result)
    result = repeat_process6(result)
    result = repeat_process7(result)
    result = repeat_process8(result)
    result = repeat_process9(result)
    result = repeat_process10(result)
    result = repeat_process11(result)
    result = repeat_process12(result)
    result = repeat_process13(result)
    result = repeat_process14(result)
    result = repeat_process15(result)
    result = repeat_process16(result)
    result = repeat_process17(result)
    result = repeat_process18(result)
    result = repeat_process19(result)
    result = repeat_process20(result)
    result = repeat_process21(result)
    result = repeat_process22(result)
    result = repeat_process23(result)
    result = repeat_process24(result)
    result = repeat_process25(result)
    result = repeat_process26(result)
    result = repeat_process27(result)
    result = repeat_process28(result)
    result = repeat_process29(result)
    result = repeat_process30(result)
    result = repeat_process31(result)
    result = repeat_process32(result)
    result = repeat_process33(result)
    result = repeat_process34(result)
    result = repeat_process35(result)
    result = repeat_process36(result)
    result = repeat_process37(result)
    result = repeat_process38(result)
    result = repeat_process39(result)
    result = repeat_process40(result)
    result = repeat_process41(result)
    result = repeat_process42(result)
    result = repeat_process43(result)
    result = repeat_process44(result)
    result = repeat_process45(result)
    result = repeat_process46(result)
    result = repeat_process47(result)
    result = repeat_process48(result)
    result = repeat_process49(result)
    result = repeat_process50(result)
    result = recursive_process(result)
    sys.stdout.write(result)

final_output()
