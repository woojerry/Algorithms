# 언휴는 도서관에서 책을 찾아주는 업무를 하고 있습니다.
# 일을 하면서 빠르게 검색하기 위해 책에 일련 번호를 부여하여 순차적으로 배치하였습니다.
# 그리고 AI 로봇에게 빠른 검색을 할 수 있게 설정하였습니다.
# 검색할 책 번호를 입력하면 전체 일련 번호의 중간 값과 비교합니다.
# 같으면 해당 책을 갖고 오고 작으면 앞쪽에 찾고 크면 뒤쪽에서 찾습니다.
# 이것을 반복하면 빠르게 찾을 수 있네요.

# 입력은 번호 순으로 정렬 상태의 컬렉션
# 반환은 검색한 순서 컬렉션와 검색 여부
# 입력: nums[2, 7, 11, 15, 22, 34, 37, 50, 120, 212, 223, 456], target = 223
# 출력: [37,212,456,223, True]

def solution(nums, target):
    re = []  # re:=빈 리스트를 생성 - 탐색 경로와 존재 여부를 보관할 컬렉션(반환할 컬렉션)
    while len(nums):  # 반복 - 검색할 대상 컬렉션의 길이가 0보다 크면 반복
        mid = len(nums)//2  # mid := 가운데 요소
        re.append(nums[mid])  # mid요소를 re에 추가
        if nums[mid] == target:  # 조건 mid요소와 target 이 일치하면
            re.append(True)  # re에 True 보관
            return re  # re 반환
        # 조건 mid요소가 target 보다 작다면(target이 mid요소보다 클 때)
        elif nums[mid] < target:
            nums = nums[mid+1:]  # nums := nums에서 mid+1 인덱스 뒤쪽에 있는 요소로 구성한 컬렉션
        else:  # 아니면(조건 mid요소가 target 보다 크면(target이 mid요소보다 작을 때))
            nums = nums[:mid]  # nums := nums에서 mid-1 인덱스 앞쪽에 있는 요소로 구성한 컬렉션
    re.append(False)  # re에 False를 보관
    return re  # re를 반환


re = solution(nums=[2, 7, 11, 15, 22, 34, 37, 50,
              120, 212, 223, 456], target=223)
print(re)
