# AI Use-Case Library
# Week 1 - Enterprise AI Track
# Format: name, industry, function, description, data_required, ai_pattern

use_cases = [
    {
        "name": "Credit Risk Scoring",
        "industry": "Banking",
        "function": "Risk & Compliance",
        "description": "Predicts likelihood of loan default using applicant financial history.",
        "data_required": "Credit history, income, debt levels, payment records",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Contract Review Assistant",
        "industry": "Legal",
        "function": "Operations",
        "description": "Extracts key clauses, flags risks, and summarises contracts.",
        "data_required": "Contract PDFs, clause taxonomy, historical redlines",
        "ai_pattern": "Reasoning"
    },
    {
        "name": "Regulatory Change Monitor",
        "industry": "Banking",
        "function": "Risk & Compliance",
        "description": "Monitors regulatory publications and flags relevant changes to compliance teams.",
        "data_required": "Regulatory feeds, internal policy documents",
        "ai_pattern": "Generation"
    },
    {
        "name": "AML Transaction Monitoring",
        "industry": "Banking",
        "function": "Risk & Compliance",
        "description": "Detects suspicious transaction patterns indicative of money laundering.",
        "data_required": "Transaction records, customer profiles, watchlists",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Employee Attrition Predictor",
        "industry": "Cross-industry",
        "function": "Human Resources",
        "description": "Predicts which employees are at risk of leaving based on engagement signals.",
        "data_required": "HR records, performance reviews, survey data, tenure",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Policy Document Assistant",
        "industry": "Government",
        "function": "Operations",
        "description": "Answers staff questions by retrieving answers from internal policy documents.",
        "data_required": "Policy documents, FAQs, procedure manuals",
        "ai_pattern": "Reasoning"
    },
    {
        "name": "Invoice Processing Automation",
        "industry": "Cross-industry",
        "function": "Finance",
        "description": "Extracts fields from invoices, validates against POs, routes for approval.",
        "data_required": "Invoice PDFs, purchase orders, supplier master data",
        "ai_pattern": "Generation"
    },
    {
        "name": "Customer Churn Predictor",
        "industry": "Telecommunications",
        "function": "Marketing",
        "description": "Identifies customers likely to cancel and triggers retention interventions.",
        "data_required": "Usage data, billing history, support tickets, NPS scores",
        "ai_pattern": "Prediction"
    },
    {
        "name": "ESG Report Generator",
        "industry": "Cross-industry",
        "function": "Sustainability",
        "description": "Drafts ESG disclosures by extracting data from operational reports.",
        "data_required": "Emissions data, energy usage, HR metrics, audit reports",
        "ai_pattern": "Generation"
    },
    {
        "name": "Fit and Proper Assessment Copilot",
        "industry": "Banking",
        "function": "Risk & Compliance",
        "description": "Assists regulators in reviewing candidate fitness and propriety submissions.",
        "data_required": "Application forms, reference letters, regulatory history",
        "ai_pattern": "Reasoning"
    },
    {
        "name": "Procurement Spend Analyser",
        "industry": "Cross-industry",
        "function": "Finance",
        "description": "Clusters spend data to identify savings opportunities and maverick spend.",
        "data_required": "Purchase orders, supplier invoices, GL codes",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Clinical Trial Document Reviewer",
        "industry": "Healthcare",
        "function": "Operations",
        "description": "Reviews clinical trial protocols and flags deviations from regulatory standards.",
        "data_required": "Trial protocols, regulatory guidelines, adverse event reports",
        "ai_pattern": "Reasoning"
    },
    {
        "name": "Carbon Project Risk Assessor",
        "industry": "Sustainability",
        "function": "Risk & Compliance",
        "description": "Evaluates carbon credit project documents for methodology and permanence risks.",
        "data_required": "Project design documents, validation reports, satellite data",
        "ai_pattern": "Reasoning"
    },
    {
        "name": "Customer Support Triage",
        "industry": "Cross-industry",
        "function": "Customer Service",
        "description": "Classifies incoming support tickets and routes to the right team automatically.",
        "data_required": "Historical tickets, resolution labels, product taxonomy",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Legal Discovery Assistant",
        "industry": "Legal",
        "function": "Operations",
        "description": "Searches and ranks documents relevant to litigation discovery requests.",
        "data_required": "Document repositories, case metadata, keyword taxonomies",
        "ai_pattern": "Reasoning"
    },
    {
        "name": "Recruitment CV Screener",
        "industry": "Cross-industry",
        "function": "Human Resources",
        "description": "Ranks candidates against job requirements and flags top matches for review.",
        "data_required": "CVs, job descriptions, historical hiring decisions",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Fraud Detection — Card Payments",
        "industry": "Banking",
        "function": "Risk & Compliance",
        "description": "Scores card transactions in real time for fraud probability.",
        "data_required": "Transaction streams, device data, merchant categories",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Infrastructure Maintenance Predictor",
        "industry": "Government",
        "function": "Operations",
        "description": "Predicts asset failure using sensor data to schedule proactive maintenance.",
        "data_required": "IoT sensor data, maintenance logs, asset registry",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Meeting Summariser",
        "industry": "Cross-industry",
        "function": "Productivity",
        "description": "Transcribes and summarises meetings, extracts action items and decisions.",
        "data_required": "Audio recordings or transcripts, attendee list",
        "ai_pattern": "Generation"
    },
    {
        "name": "Supply Chain Disruption Monitor",
        "industry": "Manufacturing",
        "function": "Operations",
        "description": "Monitors news and logistics data to flag supply chain risks proactively.",
        "data_required": "News feeds, supplier data, shipment tracking, weather data",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Research Synthesis Agent",
        "industry": "Cross-industry",
        "function": "Strategy",
        "description": "Gathers, summarises and cites information from multiple sources into a brief.",
        "data_required": "Web sources, internal reports, academic papers",
        "ai_pattern": "Reasoning"
    },
    {
        "name": "Personalised Learning Assistant",
        "industry": "Education",
        "function": "Operations",
        "description": "Adapts learning content and pace to individual student progress.",
        "data_required": "Assessment results, engagement data, curriculum maps",
        "ai_pattern": "Prediction"
    },
    {
        "name": "Insurance Claims Processor",
        "industry": "Insurance",
        "function": "Operations",
        "description": "Extracts claim details, validates policy coverage, flags anomalies for review.",
        "data_required": "Claims forms, policy documents, historical claims data",
        "ai_pattern": "Reasoning"
    },
    {
        "name": "Equity Research Copilot",
        "industry": "Banking",
        "function": "Strategy",
        "description": "Assists analysts in drafting research notes from financial data and filings.",
        "data_required": "Financial statements, earnings transcripts, market data",
        "ai_pattern": "Generation"
    },
    {
        "name": "Greening Project Planner",
        "industry": "Sustainability",
        "function": "Operations",
        "description": "Recommends species mix, planting density and sequencing for reforestation projects.",
        "data_required": "Soil data, climate data, species databases, land maps",
        "ai_pattern": "Prediction"
    },
]

def show_list(cases):
    print("\n── AI Use-Case Library ──────────────────────────────────")
    print(f"  {'#':<4} {'Use Case':<35} {'Industry':<15} {'Function'}")
    print("  " + "-" * 70)
    for i, case in enumerate(cases):
        print(f"  [{i+1}]  {case['name']:<33} {case['industry']:<15} {case['function']}")
    print(f"\n  {len(cases)} use case(s) found.\n")

def show_detail(case):
    print("\n── Use Case Detail ──────────────────────────────────────")
    print(f"  Name:        {case['name']}")
    print(f"  Industry:    {case['industry']}")
    print(f"  Function:    {case['function']}")
    print(f"  AI Pattern:  {case['ai_pattern']}")
    print(f"\n  Description:\n  {case['description']}")
    print(f"\n  Data Required:\n  {case['data_required']}")
    print("─" * 60 + "\n")


def filter_cases(cases, industries=None, functions=None):
    results = cases
    if industries:
        results = [c for c in results if any(
            ind.lower() in c['industry'].lower() for ind in industries
        )]
    if functions:
        results = [c for c in results if any(
            fn.lower() in c['function'].lower() for fn in functions
        )]
    return results


def main():
    import argparse

    parser = argparse.ArgumentParser(description="AI Use-Case Library")
    parser.add_argument("--industry", nargs="+", help="Filter by industry (one or more)")
    parser.add_argument("--function", nargs="+", help="Filter by function (one or more)")
    args = parser.parse_args()
    filtered = filter_cases(use_cases, args.industry, args.function)
    show_list(filtered)

    choice = input("  Enter a number to see details (or press Enter to exit): ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(filtered):
            show_detail(filtered[index])
        else:
            print("  Invalid number.\n")

main()