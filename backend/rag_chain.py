def generate_answer(query, docs):

    if not docs:
        return "No relevant information found."

    query = query.lower()

    for doc in docs:

        text = doc.page_content.lower()

        # Refund Policy
        if "refund" in query:
            if "refund" in text:
                return """
Customers can request a refund within 7 days of purchase.

Approved refunds are processed within 5 business days.

Refunds are not applicable for customized services, expired subscriptions, or misuse of services.
"""

        # Leave Policy
        elif "leave" in query:
            if "leave" in text:
                return """
Employees are entitled to:

• 12 Casual Leaves
• 10 Sick Leaves
• 5 Emergency Leaves

Leave requests must be submitted through the HR portal.
"""

        # Customer Support
        elif "support" in query or "contact" in query:
            if "support" in text:
                return """
Customer support is available from 9:00 AM to 6:00 PM (Monday to Saturday).

Support Channels:
• Email: support@abctech.com
• Phone: +91-9876543210
• Website Chat Support
"""

        # Work From Home
        elif "work from home" in query or "wfh" in query:
            return """
Employees are allowed to work from home up to 2 days per week with manager approval.
"""

        # Security
        elif "security" in query or "password" in query:
            return """
Employees must use strong passwords and are prohibited from sharing credentials or downloading unauthorized software.
"""

    return "Sorry, no relevant information was found in the company policy document."