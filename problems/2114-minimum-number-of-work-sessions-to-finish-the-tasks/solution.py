class Solution:
    def minSessions(self, tasks: List[int], session_time: int) -> int:
        def min_sessions(t: int, sessions: list, dp: dict) -> int:
            if (x := (t, tuple(sorted(sessions)))) in dp: return dp[x]
            
            if t == len(tasks): return len(sessions)
            
            sessions.append(tasks[t])
            min_len = min_sessions(t + 1, sessions, dp)
            sessions.pop()
            
            for i in range(len(sessions)):
                if sessions[i] + tasks[t] <= session_time:
                    sessions[i] += tasks[t]
                    min_len = min(min_len, min_sessions(t + 1, sessions, dp))
                    sessions[i] -= tasks[t]
            
            dp[(t, tuple(sorted(sessions)))] = min_len
            return min_len
        
        return min_sessions(0, [], {})
