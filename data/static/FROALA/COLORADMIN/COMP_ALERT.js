function COMP_ALERT(FroalaEditor, message) {

              FroalaEditor.DefineIcon('alert', { NAME: 'info', SVG_KEY: 'help' })

              FroalaEditor.RegisterCommand('alert', {
                title: 'Hello information',
                focus: false,
                undo: false,
                refreshAfterCallback: false,
                callback: function () {
                  alert(message)
                }
              })


}
