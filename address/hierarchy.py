from .kinds import *

hierarchy = {
    KIND_STREET_ADDRESS:  [KIND_ROUTE],
    KIND_ROUTE:           [KIND_SUBPREMISE],
    KIND_INTERSECTION:    [KIND_NEIGHBORHOOD],
    KIND_POLITICAL:       [],
    KIND_AAL1:            [KIND_COUNTRY],
    KIND_AAL2:            [KIND_AAL1],
    KIND_AAL3:            [KIND_AAL2],
    KIND_AAL4:            [KIND_AAL3],
    KIND_AAL5:            [KIND_AAL4],
    KIND_COLLOQUIAL_AREA: [KIND_AAL5],
    KIND_LOCALITY:        [KIND_AAL5],
    KIND_WARD:            [KIND_AAL5],
    KIND_SUBLOCALITY:     [KIND_LOCALITY],
    KIND_SUBLOCALITY_L1:  [KIND_SUBLOCALITY],
    KIND_NEIGHBORHOOD:    [KIND_SUBLOCALITY_L1],
    KIND_PREMISE:         [KIND_NEIGHBORHOOD],
    KIND_SUBPREMISE:      [KIND_PREMISE],
    KIND_POSTAL_CODE:     [KIND_POSTAL_TOWN],
    KIND_POSTAL_CODE_PREFIX: [KIND_POSTAL_CODE],
    KIND_NATURAL_FEATURE: [KIND_NEIGHBORHOOD],
    KIND_AIRPORT:         [KIND_NEIGHBORHOOD],
    KIND_PARK:            [KIND_NEIGHBORHOOD],
    KIND_POI:             [KIND_NEIGHBORHOOD],
    KIND_FLOOR:           [KIND_SUBPREMISE],
    KIND_ESTABLISHMENT:   [KIND_SUBPREMISE],
    KIND_PARKING:         [KIND_SUBPREMISE],
    KIND_POST_BOX:        [KIND_NEIGHBORHOOD],
    KIND_POSTAL_TOWN:     [KIND_NEIGHBORHOOD],
    KIND_ROOM:            [KIND_FLOOR],
    KIND_STREET_NUMBER:   [KIND_STREET_ADDRESS],
    KIND_BUS_STATION:     [KIND_STREET_NUMBER],
    KIND_TRAIN_STATION:   [KIND_STREET_NUMBER],
    KIND_TRANSIT_STATION: [KIND_STREET_NUMBER],
}
