'''
신규 아이디 추천 (Level 1)
https://programmers.co.kr/learn/courses/30/lessons/72410
'''

import re
'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''


def attach_ending(id):
    if len(id) <= 2:
        id = id + id[-1]
        return attach_ending(id)
    else:
        return id


def solution(new_id):
    new_id = new_id.lower()  # clause 1
    new_id = re.sub('[^a-z0-9\-\_\.]*', '', new_id)  # clause 2
    new_id = re.sub("(\.{2,})+", '.', new_id)  # clause 3
    new_id = re.sub('^(\.)|(\.)$', '', new_id)  # clause 4
    new_id = 'a' if len(new_id) == 0 else new_id  # clause 5
    new_id = new_id[0:15] if len(new_id) > 15 else new_id  # clause 6
    new_id = new_id[0:14] if new_id[-1] == "." else new_id
    new_id = attach_ending(new_id) if len(new_id) <= 2 else new_id

    return new_id


if __name__ == "__main__":
    id = "abcdefghijklmn.p"
    print(f'원래 값 ==> {id}')
    print(f'수정 값 ==> {solution(id)}')
