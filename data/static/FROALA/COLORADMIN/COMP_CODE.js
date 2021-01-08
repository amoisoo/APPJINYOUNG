function COMP_CODE(FroalaEditor) {

              FroalaEditor.DefineIcon('COMP_CODE', { NAME: 'cog', SVG_KEY: 'codeView' })
              FroalaEditor.RegisterCommand('COMP_CODE', {
                title: 'Advanced options',
                type: 'dropdown',
                focus: false,
                undo: false,
                refreshAfterCallback: true,
                options: {
                  'v1': 'primary',
                  'v2': 'secondary',
                  'v3': 'light',
                  'v4': 'sucess',
                  'v5': 'danger',
                  'v6': 'warning',
                  'v7': 'info',
                  'v8': 'dark',

                  'v9': 'yellow',
                  'v10': 'lime',
                  'v11': 'purple',
                  'v12': 'indigo',
                  'v13': 'pink',
                  'v14': 'green'
                },
                callback: function (cmd, val) {
                    console.log(val)
                    if(       val == 'v1' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-primary"   role="alert"></div><br>'  ) }
                    else if( val == 'v2' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-secondary" role="alert"></div><br>' ) }
                    else if( val == 'v3' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-light"      role="alert"></div><br>' ) }
                    else if( val == 'v4' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-success"    role="alert"></div><br>' ) }
                    else if( val == 'v5' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-danger"     role="alert"></div><br>' ) }
                    else if( val == 'v6' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-warning"    role="alert"></div><br>' ) }
                    else if( val == 'v7' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-info"       role="alert"></div><br>' ) }
                    else if( val == 'v8' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-dark"       role="alert"></div><br>' ) }

                    else if( val == 'v9' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-yellow"       role="alert"></div><br>' ) }
                    else if( val == 'v10' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-lime"       role="alert"></div><br>' ) }
                    else if( val == 'v11' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-purple"       role="alert"></div><br>' ) }
                    else if( val == 'v12' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-indigo"       role="alert"></div><br>' ) }
                    else if( val == 'v13' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-pink"       role="alert"></div><br>' ) }
                    else if( val == 'v14' ){ this.html.insert( '<div  style="margin: auto; width: 80%;" class="alert alert-green"       role="alert"></div><br>' ) }

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
