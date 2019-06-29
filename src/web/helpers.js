let library = {
   replacer: function(match, pIndent, pKey, pVal, pEnd) {
      let key = '<span class=json-key>';
      let val = '<span class=json-value>';
      let str = '<span class=json-string>';
      let r = pIndent || '';
      if (pKey)
         r = r + key + pKey.replace(/[": ]/g, '') + '</span>: ';
      if (pVal)
         r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
      return r + (pEnd || '');
      },
   prettyPrint: function(obj) {
      let jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
      return JSON.stringify(obj, null, 3)
         .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
         .replace(/</g, '&lt;').replace(/>/g, '&gt;')
         .replace(jsonLine, library.replacer);
    },
    convertJson: function(str){
      try {
          return JSON.parse(str);
      } catch (e) {
          return false;
      }
    },
    countErrors: function(str) {
      let regExp = new RegExp("ERROR", "gi");
      return (str.match(regExp) || []).length;
    },
};

export default library;
