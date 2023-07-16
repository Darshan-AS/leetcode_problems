class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        n, k = len(people), len(req_skills)

        masks = lambda: accumulate(repeat(1), lshift)
        skill_to_mask = dict(zip(req_skills, masks()))
        person_skills_m = [reduce(or_, map(skill_to_mask.get, skills), 0) for skills in people]
        
        @cache
        def smallest_team_m(req_skills_m: int) -> int:
            rem_skills_m = map(lambda m: req_skills_m & ~m, person_skills_m)
            filtered = (x for x in zip(masks(), rem_skills_m) if x[1] != req_skills_m)
            teams = (p_m | smallest_team_m(rem_m) for p_m, rem_m in filtered)
            return min(teams, key=int.bit_count) if req_skills_m else 0
        
        team_m = smallest_team_m((1 << k) - 1)
        selector = map(int, bin(team_m)[:1:-1])
        return list(compress(range(n), selector))
