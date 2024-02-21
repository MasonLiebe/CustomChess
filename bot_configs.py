# Static evaluation weights
piece_values = {
    'pawn': 1,
    'knight': 2.9,
    'bishop': 3.1,
    'rook': 5,
    'queen': 9,
    'king': 0
}

location_scores = {'pawn': [[ .00, .00, .00, .00, .00, .00, .00, .00],
                            [ .80, .80, .85, .75, 1.0, .80, .85, .90],
                            [ .10, .30, .20, .45, .40, .30, .45, .70],
                            [ .50, .50, .10, .25, .25, .10, .50, .50],
                            [ .00, .00, .20, .20, .00, .00, .00, .00],
                            [ .50,-.50,-.10, .00, .00,-.10,-.50, .50],
                            [ .50, .10, .10,-.20,-.20, .10, .10, .50],
                            [ .00, .00, .00, .00, .00, .00, .00, .00]],

                'knight':  [[-.50,-.40,-.30,-.30,-.30,-.30,-.40,-.50],
                            [-.40,-.20, .00, .00, .00, .00,-.20,-.40],
                            [-.30, .00, .10, .15, .15, .10, .00,-.30],
                            [-.30, .50, .15, .20, .20, .15, .50,-.30],
                            [-.30, .00, .15, .20, .20, .15, .00,-.30],
                            [-.30, .50, .10, .15, .15, .10, .50,-.30],
                            [-.40,-.20, .00, .50, .50, .00,-.20,-.40],
                            [-.50,-.40,-.30,-.30,-.30,-.30,-.40,-.50]],

                'bishop':  [[-.20,-.10,-.10,-.10,-.10,-.10,-.10,-.20],
                            [-.10, .00, .00, .00, .00, .00, .00,-.10],
                            [-.10, .00, .50, .10, .10, .50, .00,-.10],
                            [-.10, .50, .50, .10, .10, .50, .50,-.10],
                            [-.10, .00, .10, .10, .10, .10, .00,-.10],
                            [-.10, .10, .10, .10, .10, .10, .10,-.10],
                            [-.10, .50, .00, .00, .00, .00, .50,-.10],
                            [-.20,-.10,-.10,-.10,-.10,-.10,-.10,-.20]],

                'rook':    [[ .00, .00, .00, .00, .00, .00, .00, .00],
                            [ .05, .10, .10, .10, .10, .10, .10, .05],
                            [-.05, .00, .00, .00, .00, .00, .00,-.05],
                            [-.05, .00, .00, .00, .00, .00, .00,-.05],
                            [-.05, .00, .00, .00, .00, .00, .00,-.05],
                            [-.05, .00, .00, .00, .00, .00, .00,-.05],
                            [-.05, .00, .00, .00, .00, .00, .00,-.05],
                            [ .00, .00, .00, .50, .50, .00, .00, .00]],

                'queen':   [[-.20,-.10,-.10,-.05,-.05,-.10,-.10,-.20],
                            [-.10, .00, .00, .00, .00, .00, .00,-.10],
                            [-.10, .00, .50, .50, .50, .50, .00,-.10],
                            [-.05, .00, .50, .50, .50, .50, .00,-.05],
                            [ .00, .00, .50, .50, .50, .50, .00,-.05],
                            [-.10, .50, .50, .50, .50, .50, .00,-.10],
                            [-.10, .00, .50, .00, .00, .00, .00,-.10],
                            [-.20,-.10,-.10,-.05,-.05,-.10,-.10,-.20]],
                    
                'king':    [[-.30,-.40,-.40,-.50,-.50,-.40,-.40,-.30],
                            [-.30,-.40,-.40,-.50,-.50,-.40,-.40,-.30],
                            [-.30,-.40,-.40,-.50,-.50,-.40,-.40,-.30],
                            [-.30,-.40,-.40,-.50,-.50,-.40,-.40,-.30],
                            [-.20,-.30,-.30,-.40,-.40,-.30,-.30,-.20],
                            [-.10,-.20,-.20,-.20,-.20,-.20,-.20,-.10],
                            [ .20, .20, .00, .00, .00, .00, .20, .20],
                            [ .20, .30, .10, .00, .00, .10, .30, .20]]}


# Board evaluation parameters
evaluation_params = {
    'mobility_weight': 0.5,
    'material_weight': 0.3,
    'king_safety_weight': 0.2
}