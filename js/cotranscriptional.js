function doStepwiseAnimation(elementName, structs, duration) {
    var container = new FornaContainer(elementName, {'applyForce': false,
            'allowPanningAndZooming': true,
            "labelInterval":0,
            "initialSize": [800,800],
            "transitionDuration": duration });

    var funcs = []

        for (i = 0; i < structs.length; i++) {
            if (funcs.length === 0)
                (function(val) { funcs.push(function() { console.log('here', val, structs[val]); container.transitionRNA(structs[val]); container.setOutlineColor('white');
                                            })} )(i);
            else
                (function(val, prevFunc) { funcs.push(function() { console.log('here', val, structs[val]); container.transitionRNA(structs[val], prevFunc); container.setOutlineColor('white');
                                                      })} )(i, funcs[funcs.length-1] );
        }

    console.log('funcs', funcs);

    funcs[funcs.length-1]();
}

