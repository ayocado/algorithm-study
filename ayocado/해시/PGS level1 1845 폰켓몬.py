{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d557267b-0a08-4fad-97c7-8285a9750a8c",
   "metadata": {},
   "source": [
    "#### https://school.programmers.co.kr/learn/courses/30/lessons/1845\n",
    "\n",
    "### 폰켓몬\n",
    "\n",
    "당신은 폰켓몬을 잡기 위한 오랜 여행 끝에, 홍 박사님의 연구실에 도착했습니다. 홍 박사님은 당신에게 자신의 연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.\n",
    "홍 박사님 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분합니다. 따라서 같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다. 예를 들어 연구실에 총 4마리의 폰켓몬이 있고, 각 폰켓몬의 종류 번호가 [3번, 1번, 2번, 3번]이라면 이는 3번 폰켓몬 두 마리, 1번 폰켓몬 한 마리, 2번 폰켓몬 한 마리가 있음을 나타냅니다. 이때, 4마리의 폰켓몬 중 2마리를 고르는 방법은 다음과 같이 6가지가 있습니다.\n",
    "\n",
    "첫 번째(3번), 두 번째(1번) 폰켓몬을 선택\n",
    "첫 번째(3번), 세 번째(2번) 폰켓몬을 선택\n",
    "첫 번째(3번), 네 번째(3번) 폰켓몬을 선택\n",
    "두 번째(1번), 세 번째(2번) 폰켓몬을 선택\n",
    "두 번째(1번), 네 번째(3번) 폰켓몬을 선택\n",
    "세 번째(2번), 네 번째(3번) 폰켓몬을 선택\n",
    "이때, 첫 번째(3번) 폰켓몬과 네 번째(3번) 폰켓몬을 선택하는 방법은 한 종류(3번 폰켓몬 두 마리)의 폰켓몬만 가질 수 있지만, 다른 방법들은 모두 두 종류의 폰켓몬을 가질 수 있습니다. 따라서 위 예시에서 가질 수 있는 폰켓몬 종류 수의 최댓값은 2가 됩니다.\n",
    "당신은 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에, 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 합니다. N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.\n",
    "\n",
    "### 제한사항\n",
    "\n",
    "- nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.\n",
    "- nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.\n",
    "- 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.\n",
    "- 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c1d7aaa4-94b5-4036-88ad-c0b276e97192",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 나의 풀이\n",
    "\n",
    "def solution(nums):\n",
    "    pokemon_dict = {}\n",
    "    \n",
    "    # (key : 포켓몬 번호, value : 개수)인 딕셔너리 생성\n",
    "    for i in nums:\n",
    "        if i not in pokemon_dict:\n",
    "            pokemon_dict[i] = 1\n",
    "        else:\n",
    "            pokemon_dict[i] += 1\n",
    "    \n",
    "    # 포켓몬 사전의 종류 개수, 선택해야 하는 포켓몬 개수를 비교하여 리턴값 출력\n",
    "    if len(pokemon_dict) < len(nums)/2:\n",
    "        return len(pokemon_dict)\n",
    "    else:\n",
    "        return len(nums)/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ae4b3977-fdb7-4963-aba0-a00c96917a15",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 다른 사람 풀이 : set를 이용\n",
    "\n",
    "def solution(ls):\n",
    "    return min(len(ls)/2, len(set(ls)))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
