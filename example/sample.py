from medLayer.base.conceptlayer import ConceptLayer
from medLayer.base.event import Event
from medLayer.base.host import Host
from medLayer.base.logic.calculations import calculate_event_probability
from medLayer.base.observations import Observation
from medLayer.core.datatype.probability import Probability

human = Host("Human")
disease = ConceptLayer('Disease', 2)
symptom = ConceptLayer('Symptom', 1)

human.layers = [disease, symptom]

fever = Event('Fever')
pain = Event('Pain')
symptom.nodes.append(fever)
symptom.nodes.append(pain)

fuo = Event("FUO")
disease.nodes.append(fuo)

impossible_event = Event("Impossible")

fever_observed = Observation(fever, True)
pain_observed = Observation(pain, False)

result = calculate_event_probability(impossible_event, human, [fever_observed])
print(result)