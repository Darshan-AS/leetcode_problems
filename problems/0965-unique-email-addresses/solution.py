class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize_email(email: str) -> str:
            local_name, domain_name = email.split('@')
            normalized_local_name = local_name.split('+')[0].replace('.', '')
            return normalized_local_name + '@' + domain_name
        
        return len(set(map(normalize_email, emails)))
