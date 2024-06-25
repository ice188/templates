# given N items, W capacity, find items to grab that gives max weight <= W
# solution: let dp[i][j] = max weight of first i items without exceeding capacity j

def knapsack01(weights, values, N, W):
  # time O(NW), space O(NW)
  dp = [[0] * (W+1) for _ in (N+1)]
  for i in range(1, N+1):
    w = weights[i-1]
    v = values[i-1]
    for j in range(1, W+1):
      if j >= w:
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
      else:
        dp[i][j] = dp[i-1][j]
    return dp[N][W]

def knapsack01_space(weights, values, N, W):
  # time O(NW), space O(W)
  dp = [0] * (W+1)
  for i in range(1, N+1):
    w = weights[i-1]
    v = values[i-1]
    for j in reversed(range(w, W+1)):
      dp[j] = max(dp[j], dp[j-w]+v)
  return dp[W]

def knapsack_unbound(weights, values, N, W):
  # time O(NW), space O(NW)
  dp = [[0] * (W+1) for _ in (N+1)]
  for i in range(1, N+1):
    w = weights[i-1]
    v = values[i-1]
    for j in range(1, W+1):
      if j >= w:
        dp[i][j] = max(dp[i-1][j], dp[i][j-w])
      else:
        dp[i][j] = dp[i-1][j]
    return dp[N][W]

def knapsack_unbound_space(weights, values, N, W):
  # time O(NW), space O(W)
  dp = [0] * (W+1)
  for i in range(1, N+1):
    w = weights[i-1]
    v = values[i-1]
    for j in range(w, W+1):
      dp[j] = max(dp[j], dp[j-w]+v)
  return dp[W]




  
