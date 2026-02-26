def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    def dfs(current) :
        if len(current) > 5 :
            return
        if current :
            words.append(current)
        for i in vowels :
            dfs(current + i)
    dfs('')
    return words.index(word) + 1
============================================
재귀를 써서 단어들을 빈 리스트에 순서대로 넣는다.
이 때 한 단어의 최대 길이는 5이므로 5가 넘는 단어는 리스트에 담지 않는다.
이렇게 A 부터 UUUUU까지 전부 리스트에 담고 word가 words리스트의 몇번째 인덱스에있는지
찾아서 리턴한다. 인덱스는 0부터 시작하므로 1을 더해줘 순서를 맞춰준다.
==============================================
이 방식의 논리 자체는 쉬워서 이해가 가는데 이걸 구현하는게 어렵다.
그냥 반복문을 쓰면 AEIOU가 저장되는데 어떻게 A, AA, AAA 이렇게 순서대로 들어가는지 이해가 안간다...
