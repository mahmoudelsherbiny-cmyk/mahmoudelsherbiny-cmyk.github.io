"""Build the public English CV from confirmed career facts (ReportLab required)."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'downloads/Mahmoud_Elsherbiny_CV.pdf'
INK = colors.HexColor('#153B34')
MUTED = colors.HexColor('#485B55')
pdfmetrics.registerFont(TTFont('CV', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('CV-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('CV', normal='CV', bold='CV-Bold')
styles = {
    'name': ParagraphStyle('name',fontName='CV-Bold',fontSize=21,leading=25,textColor=INK,spaceAfter=5),
    'headline': ParagraphStyle('headline',fontName='CV-Bold',fontSize=10.5,leading=14,textColor=INK,spaceAfter=6),
    'contact': ParagraphStyle('contact',fontName='CV',fontSize=9,leading=12,textColor=MUTED,spaceAfter=2),
    'section': ParagraphStyle('section',fontName='CV-Bold',fontSize=10.8,leading=14,textColor=INK,spaceBefore=13,spaceAfter=7,keepWithNext=True),
    'body': ParagraphStyle('body',fontName='CV',fontSize=9.6,leading=12.7,spaceAfter=6),
    'job': ParagraphStyle('job',fontName='CV-Bold',fontSize=11,leading=14,textColor=INK,spaceBefore=8,spaceAfter=3,keepWithNext=True),
    'company': ParagraphStyle('company',fontName='CV',fontSize=9.5,leading=12.5,textColor=MUTED,spaceAfter=7,keepWithNext=True),
    'bullet': ParagraphStyle('bullet',fontName='CV',fontSize=9.6,leading=12.7,leftIndent=11,firstLineIndent=-9,spaceAfter=5.5),
}
story=[]
def p(text,style='body'):
    story.append(Paragraph(text,styles[style]))
def section(text):p(text,'section')
def bullet(text):p('&#8226; '+escape(text),'bullet')
def job(title,company,location,dates):
    p(escape(title),'job');p(escape(f'{company} | {location} | {dates}'),'company')

p('MAHMOUD ELSHERBINY GODA','name')
p('CHIEF ACCOUNTANT | FINANCE MANAGER','headline')
p('Madinah, Saudi Arabia | +966 51 033 1817 | <link href="mailto:Mahmoud.Elsherbiny@gmail.com" color="#153B34">Mahmoud.Elsherbiny@gmail.com</link>','contact')
p('<link href="https://melsherbiny.pp.ua/" color="#153B34">melsherbiny.pp.ua</link> | <link href="https://www.linkedin.com/in/mahmoud-elsherbiny-geek/" color="#153B34">linkedin.com/in/mahmoud-elsherbiny-geek</link>','contact')
section('PROFESSIONAL SUMMARY')
p('Finance and accounting leader with 16+ years across manufacturing, construction and project-based businesses in Saudi Arabia and Egypt. Leads budget preparation, approval and execution with departmental accountability; financial reporting, manufacturing costing, cash flow and internal controls. Prepared the 2024 and 2025 financial statements and managed external audit requirements through issuance. Leads a four-person team and translates analysis into product, pricing and collection decisions within delegated authority.')
section('CORE EXPERTISE')
p('IFRS &amp; Management Reporting | Budget Ownership &amp; Variance Analysis | Manufacturing Costing &amp; Product Profitability | Cash Flow &amp; Working Capital | Financial Close &amp; Reconciliations | Internal Controls | VAT, Zakat &amp; ZATCA Compliance | External Audit Coordination | ERP Implementation | Team Leadership')
p('<b>Systems:</b> Odoo, Microsoft Dynamics AX, Oracle, QuickBooks, Advanced Excel')
section('PROFESSIONAL EXPERIENCE')
job('Chief Accountant (Head of Financial Accounting)','Hot Plate Factory','Madinah, Saudi Arabia','Jun 2024 - Present')
for t in [
 'Lead budget preparation, approval and execution, coordinating realistic assumptions with sales, production and other department heads; obtain their sign-off and accountability for departmental figures. Analyze variances and take corrective operating decisions within delegated authority.',
 'Prepared the 2024 and 2025 financial statements and notes; managed external auditor requirements, correspondence and responses through issuance. Lead month-end and year-end close and IFRS-based financial and management reporting.',
 'Lead four staff across general accounting, receivables, inventory, and cash and banking. Assign close responsibilities and approve entries and reconciliations; escalate exceptions to the Finance Director. Discuss sales and aging almost daily and cost and production performance in monthly management meetings.',
 'Established product-level costing and investigated inventory valuation and cost-of-sales discrepancies using independent Excel calculations. Sales price-and-volume analysis led to a mix review and my recommendation to suspend a low-profitability item pending cost correction; it returned after a mold redesign. A second product was repriced. New-mold investment required owner approval.',
 'Led a nine-month Odoo implementation connecting purchasing, inventory, manufacturing, sales and accounting. Owned requirements, partner negotiation and coordination, financial and operational configuration, and data migration with specialist partner support. Recreated a full year of transactions in parallel, reaching same-day entry across legacy and new systems.',
 'Recommended and followed a mold redesign with technical specialists. Reported scrap per operating hour fell 70%; internal before/after comparisons indicated approximately 39% lower unit cost, including changes in product weight and scrap.',
 'Negotiated a 2% settlement discount on overdue customer receivables within delegated authority. The customer paid on the day of negotiation; funds appeared in the bank account the following day.',
 'Manage VAT, Zakat and ZATCA compliance and strengthen policies and controls over AR/AP, banks, inventory, fixed assets and manufacturing costs.'
]:bullet(t)

story.append(PageBreak())
section('PROFESSIONAL EXPERIENCE - CONTINUED')
job('Finance Manager','Nejmet Elbayan for Construction','Abha, Saudi Arabia','Aug 2022 - May 2024')
for t in [
 'Managed project accounting, budgets, cost estimates, cost monitoring, working capital and financial reporting in coordination with project teams.',
 'Introduced a close calendar and checklist with task owners. Reduced close-to-report-submission time from 10 to 5 to 3 working days across three consecutive monthly closes. Reports went to the Finance Director for review on day 3; exceptional cycles required up to 5 working days.',
 'Prepared monthly cash forecasts covering 45-90 days. Identified a funding gap around the first quarterly loan installment and other commitments, rebuilt the cash budget and negotiated early settlement within delegated authority. Funds were available 25 days before the requirement.',
 'Monitored receivable aging and collection quality, supplier and subcontractor payments, and project variances; implemented cost controls to support management decisions and profitability.'
]:bullet(t)
job('Chief Accountant','Smile Factory','Mansoura, Egypt','Jan 2018 - Jun 2022')
for t in [
 'Led budgeting, forecasting, cost-reduction initiatives, financial analysis and weekly, monthly and quarterly reporting to senior management.',
 'Managed balance sheet reconciliations, capital expenditure monitoring, production and inventory reporting, and financial policies and controls. Served as a key contact for system audits and ERP financial processes.'
]:bullet(t)
job('Senior Accountant','Kayan Alrasheed Interior Design & Furniture','Dammam, Saudi Arabia','Jun 2014 - Apr 2017')
for t in [
 'Managed project accounting, AP/AR, supplier invoices, customer collections and reconciliations for projects and showroom operations.',
 'Prepared project cost sheets for materials, labor, installation and subcontractors; monitored budgets, inventory and purchases. Produced monthly financial reports, cash flow updates and project profitability analyses.'
]:bullet(t)
job('Cost & Managerial Accountant','Al Shamry Plastic Factory','Riyadh, Saudi Arabia','May 2010 - Apr 2014')
for t in [
 'Prepared financial statements, budgets and management reports; reviewed and approved records and reconciliations before submission to management. Managed cash flow, collections and bank relationships, and supported controls, risk assessment, administration and governmental compliance.'
]:bullet(t)
job('System Analyst & Accounting Trainer','New Vision Integrated Systems (Yusuf Abdullah Juffali Group)','Riyadh, Saudi Arabia','Dec 2009 - Apr 2010')
bullet('Trained accountants on general ledger, inventory and fixed asset modules; configured accounting systems and supported reporting, error resolution, year-end close and data validation.')
section('EDUCATION & PROFESSIONAL DEVELOPMENT')
p('<b>CMA studies - Institute of Management Accountants (IMA):</b> Part 1 passed; Part 2 in progress. Certification not yet complete.')
p('<b>Bachelor of Commerce (Accounting)</b> - Mansoura University, Egypt | 2009')
section('LANGUAGES')
p('Arabic: Native | English: Advanced')

def footer(canvas, doc):
    canvas.saveState();canvas.setFont('CV',8);canvas.setFillColor(MUTED)
    canvas.drawRightString(A4[0]-39,24,f'Mahmoud Elsherbiny | {doc.page}')
    canvas.restoreState()

doc=SimpleDocTemplate(str(OUTPUT),pagesize=A4,rightMargin=39,leftMargin=39,topMargin=34,bottomMargin=36,title='Mahmoud Elsherbiny - Finance and Accounting CV',author='Mahmoud Elsherbiny')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUTPUT)
