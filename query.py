drug_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>
PREFIX mesh: <http://id.nlm.nih.gov/mesh/>

SELECT DISTINCT ?drug ?Label ?identifier ?pharmacologicalActionLabel
WHERE {
    ?drug rdfs:label ?Label.
    ?drug meshv:identifier ?identifier.
    ?drug meshv:active true.
    ?drug meshv:pharmacologicalAction ?pharmacologicalAction.
    ?pharmacologicalAction rdfs:label ?pharmacologicalActionLabel.
    ?pharmacologicalAction meshv:broaderDescriptor* mesh:D045506.
}
order by ?Label
"""

muscular_conditions_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>
PREFIX mesh: <http://id.nlm.nih.gov/mesh/>

SELECT DISTINCT ?condition ?Label ?identifier 
WHERE {
    ?condition rdfs:label ?Label.
    ?condition meshv:active true.
    ?condition meshv:identifier ?identifier.
    ?condition meshv:broaderDescriptor* mesh:D009140.
    ?condition meshv:allowableQualifier ?allowableQualifier.
    filter (?allowableQualifier = mesh:Q000175)
    filter (lang(?Label) = 'en')
}
order by ?Label
"""

nervous_conditions_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>
PREFIX mesh: <http://id.nlm.nih.gov/mesh/>

SELECT DISTINCT ?condition ?Label ?identifier 
WHERE {
    ?condition rdfs:label ?Label.
    ?condition meshv:active true.
    ?condition meshv:identifier ?identifier.
    ?condition meshv:broaderDescriptor* mesh:D009422.
    ?condition meshv:allowableQualifier ?allowableQualifier.
    filter (?allowableQualifier = mesh:Q000175)
    filter (lang(?Label) = 'en')
}
order by ?Label
"""
