from django.shortcuts import render


def investor_relations(request):
    """Investor Relations page - for investors and analysts"""
    return render(request, 'corporate/investor_relations.html')


def cma_filings(request):
    """CMA Filings page - for regulators and compliance officers"""
    return render(request, 'corporate/cma_filings.html')


def nse_disclosures(request):
    """NSE Disclosures page - for market regulators and traders"""
    return render(request, 'corporate/nse_disclosures.html')


def annual_reports(request):
    """Annual Reports page - for investors, analysts, and stakeholders"""
    return render(request, 'corporate/annual_reports.html')


def independent_valuations(request):
    """Independent Valuations page - for regulators and investors"""
    return render(request, 'corporate/independent_valuations.html')