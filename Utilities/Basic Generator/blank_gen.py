################################################################################
#
#	blank_gen.py
#	A barebones D&D Monster Generator using statblock5e 
#	Only the monster name is filled in, all other monster information must be
#	inserted into the code manually. 
#
#	Usage: python blank_gen.py [monster name]
#		If there is a space ine the monster name, for example: chain devil
#		Use a period instead of space. That is: chain.devil 
#	
#	This generator is developed by Shunman Tse (RiasKlein)
#		https://github.com/riasklein
#	Statblock5e code is by Val Markovic (Valloric) 
#		https://github.com/Valloric
#
#	Version 1.3
#
################################################################################

import sys

# print_usage_instructions
#	Function prints the usage instructions
def print_usage_instructions ():
	print ("Correct Usage:\tpython blank_gen.py [monster name]")

if len(sys.argv) < 2:
	print ("Usage Error:\tThe program needs a monster name.")
	print_usage_instructions()
	sys.exit()

# According to the usage instructions, the monster name is the second argument
monster_name = sys.argv[1]				# Get the monster name from arguments

# Convert periods to spaces
monster_name = monster_name.replace ('.', ' ')

# Capitalize the first letter of every word in monster name
list = [word[0].upper() + word[1:] for word in monster_name.split()]
monster_name = " ".join(list)

# Now we must create a HTML file with that monster's name
filew = open (monster_name.lower() + ".html", 'w')

################################################################################
# Writing the formatting code into the HTML file
################################################################################

filew.write(
"""<!DOCTYPE html>
<html><head><link href="https://fonts.googleapis.com/css?family=Libre+Baskerville:700" rel="stylesheet" type="text/css"/><link href="http://fonts.googleapis.com/css?family=Noto+Sans:400,700,400italic,700italic" rel="stylesheet" type="text/css"/><meta charset="utf-8"/>
<title>""")

filew.write(monster_name)

filew.write(
"""</title><style>
      body {
        margin: 0;
      }

      stat-block {
        margin-left: 20px;
        margin-top: 20px;
      }
    </style></head><body><template id="tapered-rule">
	<style>
    svg {
      fill: #922610;
      stroke: #922610;
      margin-top: 0.6em;
      margin-bottom: 0.35em;
    }
  </style>
  <svg height="5" width="400">
    <polyline points="0,0 400,2.5 0,5"></polyline>
  </svg>
</template><script>
(function(window, document) {
  var elemName = 'tapered-rule';
  var thatDoc = document;
  var thisDoc = (thatDoc.currentScript || thatDoc._currentScript).ownerDocument;
  var proto = Object.create(HTMLElement.prototype, {
    createdCallback: {
      value: function() {
        var template = thisDoc.getElementById(elemName);
        var clone = thatDoc.importNode(template.content, true);
        this.createShadowRoot().appendChild(clone);
      }
    }
  });
  thatDoc.registerElement(elemName, {prototype: proto});
})(window, document);
</script><template id="top-stats">
  <style>
    ::content * {
      color: #7A200D;
    }
  </style>

  <tapered-rule></tapered-rule>
  <content></content>
  <tapered-rule></tapered-rule>
</template><script>
(function(window, document) {
  var elemName = 'top-stats';
  var thatDoc = document;
  var thisDoc = (thatDoc.currentScript || thatDoc._currentScript).ownerDocument;
  var proto = Object.create(HTMLElement.prototype, {
    createdCallback: {
      value: function() {
        var template = thisDoc.getElementById(elemName);
        var clone = thatDoc.importNode(template.content, true);
        this.createShadowRoot().appendChild(clone);
      }
    }
  });
  thatDoc.registerElement(elemName, {prototype: proto});
})(window, document);
</script><template id="creature-heading">
  <style>
    ::content > h1 {
      font-family: 'Libre Baskerville', 'Lora', 'Calisto MT',
                   'Bookman Old Style', Bookman, 'Goudy Old Style',
                   Garamond, 'Hoefler Text', 'Bitstream Charter',
                   Georgia, serif;
      color: #7A200D;
      font-weight: 700;
      margin: 0px;
      font-size: 23px;
      letter-spacing: 1px;
      font-variant: small-caps;
    }

    ::content > h2 {
      font-weight: normal;
      font-style: italic;
      font-size: 12px;
      margin: 0;
    }
  </style>
  <content select="h1"></content>
  <content select="h2"></content>
</template><script>
(function(window, document) {
  var elemName = 'creature-heading';
  var thatDoc = document;
  var thisDoc = (thatDoc.currentScript || thatDoc._currentScript).ownerDocument;
  var proto = Object.create(HTMLElement.prototype, {
    createdCallback: {
      value: function() {
        var template = thisDoc.getElementById(elemName);
        var clone = thatDoc.importNode(template.content, true);
        this.createShadowRoot().appendChild(clone);
      }
    }
  });
  thatDoc.registerElement(elemName, {prototype: proto});
})(window, document);
</script><template id="abilities-block">
  <style>
    table {
      width: 100%;
      border: 0px;
      border-collapse: collapse;
    }
    th, td {
      width: 50px;
      text-align: center;
    }
  </style>
  <tapered-rule></tapered-rule>
  <table>
    <tbody><tr>
      <th>STR</th>
      <th>DEX</th>
      <th>CON</th>
      <th>INT</th>
      <th>WIS</th>
      <th>CHA</th>
    </tr>
    <tr>
      <td id="str"></td>
      <td id="dex"></td>
      <td id="con"></td>
      <td id="int"></td>
      <td id="wis"></td>
      <td id="cha"></td>
    </tr>
  </tbody></table>
  <tapered-rule></tapered-rule>
</template><script>
(function(window, document) {
  function abilityModifier(abilityScore) {
    var score = parseInt(abilityScore, 10);
    return Math.floor((score - 10) / 2);
  }

  function formattedModifier(abilityModifier) {
    if (abilityModifier >= 0) {
      return '+' + abilityModifier;
    }
    // This is an en dash, NOT a "normal" dash. The minus sign needs to be more visible.
    return unescape('%u2013') + Math.abs(abilityModifier);
  }

  function abilityText(abilityScore) {
    return [String(abilityScore),
            ' (',
            formattedModifier(abilityModifier(abilityScore)),
            ')'].join('');
  }

  var elemName = 'abilities-block';
  var thatDoc = document;
  var thisDoc = (thatDoc.currentScript || thatDoc._currentScript).ownerDocument;
  var proto = Object.create(HTMLElement.prototype, {
    createdCallback: {
      value: function() {
        var template = thisDoc.getElementById(elemName);
        var clone = thatDoc.importNode(template.content, true);
        var root = this.createShadowRoot().appendChild(clone);
      }
    },
    attachedCallback: {
      value: function() {
        var root = this.shadowRoot;
        for (var i = 0; i < this.attributes.length; i++) {
          var attribute = this.attributes[i];
          var abilityShortName = attribute.name.split('-')[1];
          root.getElementById(abilityShortName).textContent =
             abilityText(attribute.value);
        }

      }
    }
  });
  thatDoc.registerElement(elemName, {prototype: proto});
})(window, document);
</script><template id="property-block">
  <style>
    :host {
      margin-top: 0.3em;
      margin-bottom: 0.9em;
      line-height: 1.5;
      display: block;
    }

    ::content > h4 {
      margin: 0;
      display: inline;
      font-weight: bold;
      font-style: italic;
    }

    ::content > p:first-of-type {
      display: inline;
      text-indent: 0;
    }

    ::content > p {
      text-indent: 1em;
      margin: 0;
    }
  </style>
  <content></content>
</template><script>
(function(window, document) {
  var elemName = 'property-block';
  var thatDoc = document;
  var thisDoc = (thatDoc.currentScript || thatDoc._currentScript).ownerDocument;
  var proto = Object.create(HTMLElement.prototype, {
    createdCallback: {
      value: function() {
        var template = thisDoc.getElementById(elemName);
        var clone = thatDoc.importNode(template.content, true);
        this.createShadowRoot().appendChild(clone);
      }
    }
  });
  thatDoc.registerElement(elemName, {prototype: proto});
})(window, document);
</script><template id="property-line">
  <style>
    :host {
      line-height: 1.4;
      display: block;
      text-indent: -1em;
      padding-left: 1em;
    }

    ::content > h4 {
      margin: 0;
      display: inline;
      font-weight: bold;
    }

    ::content > p:first-of-type {
      display: inline;
      text-indent: 0;
    }

    ::content > p {
      text-indent: 1em;
      margin: 0;
    }
  </style>
  <content></content>
</template><script>
(function(window, document) {
  var elemName = 'property-line';
  var thatDoc = document;
  var thisDoc = (thatDoc.currentScript || thatDoc._currentScript).ownerDocument;
  var proto = Object.create(HTMLElement.prototype, {
    createdCallback: {
      value: function() {
        var template = thisDoc.getElementById(elemName);
        var clone = thatDoc.importNode(template.content, true);
        this.createShadowRoot().appendChild(clone);
      }
    }
  });
  thatDoc.registerElement(elemName, {prototype: proto});
})(window, document);
</script><template id="stat-block">
  <style>
    .bar {
      height: 5px;
      background: #E69A28;
      border: 1px solid #000;
      position: relative;
      z-index: 1;
    }

    :host {
      display: inline-block;
    }

    #content-wrap {
      font-family: 'Noto Sans', 'Myriad Pro', Calibri, Helvetica, Arial,
                    sans-serif;
      font-size: 13.5px;
      background: #FDF1DC;
      padding: 0.6em;
      padding-bottom: 0.5em;
      border: 1px #DDD solid;
      box-shadow: 0 0 1.5em #867453;

      /* We don't want the box-shadow in front of the bar divs. */
      position: relative;
      z-index: 0;

      /* Leaving room for the two bars to protrude outwards */
      margin-left: 2px;
      margin-right: 2px;

      /* This is possibly overriden by next CSS rule. */
      width: 400px;

      -webkit-columns: 400px;
         -moz-columns: 400px;
              columns: 400px;
      -webkit-column-gap: 40px;
         -moz-column-gap: 40px;
              column-gap: 40px;

      /* When height is constrained, we want sequential filling of columns. */
      -webkit-column-fill: auto;
         -moz-column-fill: auto;
              column-fill: auto;
    }

    :host([data-two-column]) #content-wrap {
      /* One column is 400px and the gap between them is 40px. */
      width: 840px;
    }

    ::content > h3 {
      border-bottom: 1px solid #7A200D;
      color: #7A200D;
      font-size: 21px;
      font-variant: small-caps;
      font-weight: normal;
      letter-spacing: 1px;
      margin: 0;
      margin-bottom: 0.3em;

      break-inside: avoid-column;
      break-after: avoid-column;
    }

    /* For user-level p elems. */
    ::content > p {
      margin-top: 0.3em;
      margin-bottom: 0.9em;
      line-height: 1.5;
    }

    /* Last child shouldn't have bottom margin, too much white space. */
    ::content > *:last-child {
      margin-bottom: 0;
    }
  </style>
  <div class="bar"></div>
  <div id="content-wrap">
    <content></content>
  </div>
  <div class="bar"></div>
</template><script>
(function(window, document) {
  var elemName = 'stat-block';
  var thatDoc = document;
  var thisDoc = (thatDoc.currentScript || thatDoc._currentScript).ownerDocument;
  var proto = Object.create(HTMLElement.prototype, {
    createdCallback: {
      value: function() {
        var template = thisDoc.getElementById(elemName);
        // If the attr() CSS3 function were properly implemented, we wouldn't
        // need this hack...
        if (this.hasAttribute('data-content-height')) {
          var wrap = template.content.getElementById('content-wrap');
          wrap.style.height = this.getAttribute('data-content-height') + 'px';
        }
        var clone = thatDoc.importNode(template.content, true);
        this.createShadowRoot().appendChild(clone);
      }
    }
  });
  thatDoc.registerElement(elemName, {prototype: proto});
})(window, document);
</script>
"""
)

################################################################################
# Writing the monster stats into the file
################################################################################

filew.write("""
<stat-block>
    <creature-heading>
      <h1>""")

filew.write(monster_name)

filew.write("""</h1>
      <h2>
	  
	  </h2>
    </creature-heading>

    <top-stats>
      <property-line>
        <h4>Armor Class</h4>
        <p> 
		
		</p>
      </property-line>
	  
      <property-line>
        <h4>Hit Points</h4>
        <p> 
		
		</p>
      </property-line>
	  
      <property-line>
        <h4>Speed</h4>
        <p>
		
		</p>
      </property-line>

      <abilities-block data-str="1" data-dex="1" data-con="1" data-int="1" data-wis="1" data-cha="1" ></abilities-block>

	  <property-line>
        <h4>Saving Throws</h4>
        <p>
		
		</p>
      </property-line>

      <property-line>
        <h4>Skills</h4>
        <p>
		
		</p>
      </property-line>

	  <property-line>
        <h4>Damage Resistances</h4>
        <p>
		
		</p>
      </property-line>
	  
	  <property-line>
        <h4>Damage Immunities</h4>
        <p>
		
		</p>
      </property-line>
	  
	  <property-line>
        <h4>Damage Vulnerabilities</h4>
        <p>
		
		</p>
      </property-line>

	  <property-line>
        <h4>Condition Immunities</h4>
        <p>
		
		</p>
      </property-line>

      <property-line>
        <h4>Senses</h4>
		<p>
		
		</p>
      </property-line>
	  
      <property-line>
        <h4>Languages</h4>
        <p>
		
		</p>
      </property-line>
	  
      <property-line>
        <h4>Challenge</h4>
        <p>
		
		</p>
      </property-line>
    </top-stats>
	
	<property-block>
		<h4>
		
		</h4>
		<p>	
		</p>
    </property-block>
	
	<property-block>
		<h4>
		
		</h4>
		<p>	
		</p>
    </property-block>
		
    <h3>Actions</h3>
	
	<property-block>
		<h4>
		
		</h4>
		<p>	
		</p>
    </property-block>
	
	<property-block>
		<h4>
		
		</h4>
		<p><i>Melee Weapon Attack:</i> 
		<i>Hit:</i> 
		</p>
    </property-block>
	
	<property-block>
		<h4>
		
		</h4>
		<p><i>Ranged Weapon Attack:</i> 
		<i>Hit:</i> 
		</p>
    </property-block>

  </stat-block></body></html>
""")

filew.close()		# Closing the opened file
