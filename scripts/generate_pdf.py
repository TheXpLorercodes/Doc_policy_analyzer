from fpdf import FPDF
import os

def create_policy_pdf(output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Global Corp Leave Policy", ln=True, align="C")
    
    # Body
    pdf.set_font("Arial", size=12)
    
    policy_texts = [
        "1. Annual Leave: Every employee is entitled to 20 days of paid annual leave per year.",
        "2. Sick Leave: Employees receive 10 days of paid sick leave annually. Unused sick leave does not roll over.",
        "3. Maternity Leave: 16 weeks of fully paid maternity leave are provided to eligible employees.",
        "4. Paternity Leave: 4 weeks of fully paid paternity leave are available for secondary caregivers.",
        "5. Bereavement Leave: Employees are granted up to 5 days of paid leave in the event of a death in the immediate family.",
        "6. Remote Work: Employees are permitted to work remotely up to 2 days per week, subject to manager approval.",
        "7. Core Hours: Core working hours are from 10:00 AM to 3:00 PM in the employee's local time zone."
    ]

    for item in policy_texts:
        pdf.cell(200, 10, txt=item, ln=True)

    pdf.output(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    os.makedirs(os.path.join(os.path.dirname(__file__), "..", "data"), exist_ok=True)
    pdf_path = os.path.join(os.path.dirname(__file__), "..", "data", "policy.pdf")
    create_policy_pdf(pdf_path)
