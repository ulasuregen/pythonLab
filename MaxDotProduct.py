def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def minimumDeleteSum(s1, s2):
    s1,s2 = (s1,s2) if len(s1) >= len(s2) else (s2,s1) # s1 >= s2
    dp = [[''for k in range(len(s1)+1)] for _ in range(len(s2)+1)]

    i = len(s2) - 1
    j = len(s1) - 1
    
    while i >= 0:
        temp_s1 = s1[j:]
        temp_s2 = s2[i:]

        # print('invest: {} - {}'.format(temp_s1, temp_s2))
        has_match = False

        for k in range(len(temp_s2)):
            

            if temp_s1[0] == temp_s2[k]:
                has_match = True
                t1 = temp_s1[0]+dp[i+k+1][j+1]
                t2 = dp[i][j+1]

                val_t1 = sum(map(ord,t1))
                val_t2 = sum(map(ord,t2))

                s = t1 if val_t1 >= val_t2 else t2

                if sum(map(ord,dp[i][j])) < sum(map(ord,s)):
                    dp[i][j] = s
                
                break
            
        if not has_match:
            dp[i][j] = dp[i][j+1]

        
    
        if j > 0:
            j -= 1
        else:
            i -= 1
            j = len(s1)-1
        
    print(dp[0][0])
    
    return sum(map(ord,s1)) + sum(map(ord,s2)) - 2*sum(map(ord, dp[0][0]))


    


s1 = "rydcwbmaeefsdnhocwowzgocvqzpagmtauzxhprovogzmqemsocnbsqkndslmfhdshhaikejjzssmzhjacxrecpwumlxquclgimrhedcjcymaxvwcoeibrxbqwsjyfdjlqazpxjikcftjyeoqgettvquyqucnpyqcqukmsvbpjqzixubauzlfofomzjqrqglxbybhcxnamzdmvkiepqpyfthrduhgcznyima"
s2 = "ukzcpbrrcrjpncxmxsbmxjvedksomkubzfbcpjvlrpzhxecxouflcwncfczgulbvuyueliacrcktutcpjlzxjvwwncdaswohfymhusuxrkdqkzaymewqkmzzzgehmgxzhqiapqzjpfuupuznbfkpdblqlmiuwordgqpirkzzykgqnxcqogatrmhhqqbjhxhpvqpfkndhhxiffaxhtzdjnrkboxexpvtsnxrlivifhjacpczbmanvrfmwbpzsfnfxmrpcavlfkhgsasqxbgmlplmmfwjggmkfjyedudjiceoguetbbluzkqmmgapwlwxafwqvzwlbhahbxkvtbeoiohzzubpmbfezbuvxhcwuriwmnbwnvthxxqrcecgniwjrzxalvqvnzbopqogiafwjkvbxzfghglrpactcrn"
v = minimumDeleteSum(s1,s2)

print(v)

