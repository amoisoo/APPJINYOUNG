


function COMP_BOX(FroalaEditor) {
             var table_1 = '<table align="center" class="table table-sm mb-0 table-bordered table-width-80" >\n' +
                      '\t<tbody>\n' +
                      '\t\t<tr>\n' +
                      '\t\t\t<td style="width: 100%; background-color: rgb(255, 255, 255);"></td>\n' +

                      '\t\t</tr>\n' +

                      '\t</tbody>\n' +
                      '</table><br/>\n'


             var table_2 = '<table align="center" class="table table-sm mb-0 table-bordered table-width-80" >\n' +
                      '\t<tbody>\n' +
                      '\t\t<tr>\n' +
                      '\t\t\t<td style="width: 100%; background-color: rgb(242, 243, 244);"></td>\n' +

                      '\t\t</tr>\n' +

                      '\t</tbody>\n' +
                      '</table><br/>\n'


             var table_3= '<table align="center" class="table table-sm mb-0 table-bordered table-width-80" >\n' +
                      '\t<tbody>\n' +
                      '\t\t<tr>\n' +
                      '\t\t\t<td style="color:white width: 100%; background-color: #1B2024;"><span style="color: #00ACAC;"> </span></td>\n' +

                      '\t\t</tr>\n' +

                      '\t</tbody>\n' +
                      '</table><br/>\n'
            var table_4 = '<blockquote class="blockquote text-center">\n' +
                '\t<p class="mb-0">TITLE</p>\n' +
                '\t<footer class="blockquote-footer">\n' +
                '\t\t<br><br>&nbsp;</footer>\n' +
                '</blockquote>'

            var table_5 = '<div class="note note-yellow  note-with-right-icon"><div class="note-icon  text-white"><i class="fa fa-lightbulb"></i></div><div class="note-content text-right"><h4 style="text-align: left;"><strong>aaa!</strong></h4><p style="text-align: left;">BBB</p></div></div>'

            var table_6 = '<table align="center" class="table  mb-0 table-bordered table-width-80" >\n' +
                      '\t<tbody>\n' +
                      '\t\t<tr>\n' +
                      '\t\t\t<td style="width: 100%; background-color: rgb(242, 243, 244);"></td>\n' +

                      '\t\t</tr>\n' +
                      '\t\t<tr>\n' +
                      '\t\t\t<td style="width: 100%; background-color: rgb(223, 224, 226);"></td>\n' +

                      '\t\t</tr>\n' +
                      '\t</tbody>\n' +
                      '</table><br/>\n'

            var Youtube = '<div align="center">\n' +
                '\t<iframe width="640" height="480" src="https://www.youtube.com/embed/ctZ2pgcavd0" frameborder="0" allowfullscreen=""></iframe>\n' +
                '</div>'





              FroalaEditor.DefineIcon('COMP_BOX', { NAME: 'plus', SVG_KEY: 'tableStyle' })
              FroalaEditor.RegisterCommand('COMP_BOX', {
                title: 'Box',
                type: 'dropdown',
                focus: false,
                undo: false,
                refreshAfterCallback: true,
                options: {
                  'v1': 'White',
                  'v2': 'Gray',
                  'v6': 'Code',
                  'v3': 'Dark',
                  'v4': 'Blockquote',
                  'v5': 'Note',
                  'v7': 'Table 7',
                  'v8': 'Youtube'
                },
                callback: function (cmd, val) {
                    console.log(val)
                    if(       val == 'v1' ){ this.html.insert( table_1 ) }
                    else if( val == 'v2' ){ this.html.insert( table_2 ) }
                    else if( val == 'v3' ){ this.html.insert( table_3 ) }
                    else if( val == 'v4' ){ this.html.insert( table_4 ) }
                    else if( val == 'v5' ){ this.html.insert( table_5 ) }
                    else if( val == 'v6' ){ this.html.insert( table_6 ) }
                    else if( val == 'v7' ){ this.html.insert( table_5 ) }
                    else if( val == 'v8' ){ this.html.insert( Youtube ) }


                },
                // Callback on refresh.
                refresh: function ($btn) {
                  console.log('do refresh')
                },
                // Callback on dropdown show.
                refreshOnShow: function ($btn, $dropdown) {
                  console.log('do refresh when show')
                }
              })


}
