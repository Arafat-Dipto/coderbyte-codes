def MinWindowSubstring(strArr): 
  M = strArr[0]
  N = strArr[1] 
  minWindow = [-1,-1]
  # The begin and end position (both inclusive) of current window
  begin = -1
  end = 0
  # The number of each char in current window
  totalCount = {i:0 for i in N}
  # Compute the char distribution in T
  need = {}
  for item in N:  need[item] = need.get(item, 0) + 1
  # Find the first window, containing all the characters in T
  needCount = len(N)
  while end < len(M):
      if M[end] in need:
          if begin == -1:         begin = end
          totalCount[M[end]] += 1
          if totalCount[M[end]] <= need[M[end]]:
              # Find one more char for a qualified window
              needCount -= 1
              # Enough chars to form a window
              if needCount == 0:  break
      end += 1
  else:
      # Did not find a window
      return ""
  # Try to minimize the window length by removing the leftmost items
  while True:
      if M[begin] in need:
          if totalCount[M[begin]] > need[M[begin]]:
              totalCount[M[begin]] -= 1
              begin += 1
          else:
              # Already be minimum
              break
      else:
          begin += 1
  minWindow = [begin, end]
  # Try next window, ending with S[begin]
  while True:
      # Find the next window, ending with current S[begin]
      end += 1
      while end < len(M):
          if M[end] == M[begin]:      break
          if M[end] in totalCount:    totalCount[M[end]] += 1
          end += 1
      else:
          # No windows left.
          break
      # Minimize current window, by removing the leftmost items
      begin += 1
      while begin <= end:
          if M[begin] in need:
              if totalCount[M[begin]] > need[M[begin]]:
                  totalCount[M[begin]] -= 1
                  begin += 1
              else:
                  # Minimized
                  break
          else:
              begin += 1
      if end - begin < minWindow[1] - minWindow[0]:
          # Find a shorter window
          minWindow[0], minWindow[1] = begin, end
  return M[minWindow[0]: minWindow[1]+1]
# keep this function call here  
print MinWindowSubstring(raw_input())