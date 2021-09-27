class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def base_email(email: str) -> str:
            local_name, domain_name, *_ = email.split('@')
            base_local_name = ''.join(filter(lambda ch: ch != '.', local_name.split('+')[0]))
            return base_local_name + '@' + domain_name
        
        return len(set(map(base_email, emails)))
