var MQ = MathQuill.getInterface(2);
(function (factory) {
	/* global define */
	if (typeof define === 'function' && define.amd) {
		// AMD. Register as an anonymous module.
		define(['jquery'], factory);
	} else if (typeof module === 'object' && module.exports) {
		// Node/CommonJS
		module.exports = factory(require('jquery'));
	} else {
		// Browser globals
		factory(window.jQuery);
	}
}(function ($) {

	// Extends plugins for adding equation.
	//  - plugin is external module for customizing.
	$.extend($.summernote.plugins, {
		/**
		 * @param {Object} context - context object has status of editor.
		 */
		'equation': function (context) {
			var self = this;

			// ui has renders to build ui elements.
			//  - you can create a button with `ui.button`
			var ui = $.summernote.ui;

			// add equation button
			context.memo('button.equation', function () {
				// create button
				var button = ui.button({
					contents: '<i class="tiny material-icons" style="margin-top: 0.4rem;">functions</i>',
					// contents: '<i class="material-icons">functions</i>',
					tooltip: 'LaTeX Equation',

					// Might not work in modals?
					container: 'body',
					target: 'body',

					click: function () {
						self.$panel.show();
						self.$panel.hide(500);
						// invoke insertText method with 'equation' on editor module.
						var $span = $('<span>', {
							//'class': 'math',
							'contenteditable': 'false'}
						).text('');
						var $p = $('<p>').append($span);

						context.invoke('editor.insertNode', $p[0]);

						//MQ.StaticMath($span[0]);
						MQ.MathField($span[0], {
							autoCommands: 'pi theta'
						});
					}
				});

				// create jQuery object from button instance.
				var $equation = button.render();
				return $equation;
			});

			this.$
			// This events will be attached when editor is initialized.
			this.events = {
				// This will be called after modules are initialized.
				'summernote.init': function (we, e) {
					// console.log('summernote initialized', we, e);
				},
				// This will be called when user releases a key on editable.
				'summernote.keyup': function (we, e) {
					// console.log('summernote keyup', we, e);
				}
			};

			// This method will be called when editor is initialized by $('..').summernote();
			// You can create elements for plugin
			this.initialize = function () {
				this.$panel = $('<div class="equation-panel"/>').css({
					position: 'absolute',
					width: 100,
					height: 100,
					left: '50%',
					top: '50%',
					background: 'red'
				}).hide();

				this.$panel.appendTo('body');
			};

			// This methods will be called when editor is destroyed by $('..').summernote('destroy');
			// You should remove elements on `initialize`.
			this.destroy = function () {
				this.$panel.remove();
				this.$panel = null;
			};
		}
	});
}));
