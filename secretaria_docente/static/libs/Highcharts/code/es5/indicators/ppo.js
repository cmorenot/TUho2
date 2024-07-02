!/**
 * Highstock JS v11.4.1 (2024-04-04)
 *
 * Indicator series type for Highcharts Stock
 *
 * (c) 2010-2024 Wojciech Chmiel
 *
 * License: www.highcharts.com/license
 */function(t){"object"==typeof module&&module.exports?(t.default=t,module.exports=t):"function"==typeof define&&define.amd?define("highcharts/indicators/ppo",["highcharts","highcharts/modules/stock"],function(e){return t(e),t.Highcharts=e,t}):t("undefined"!=typeof Highcharts?Highcharts:void 0)}(function(t){"use strict";var e=t?t._modules:{};function o(t,e,o,r){t.hasOwnProperty(e)||(t[e]=r.apply(null,o),"function"==typeof CustomEvent&&window.dispatchEvent(new CustomEvent("HighchartsModuleLoaded",{detail:{path:e,module:t[e]}})))}o(e,"Stock/Indicators/PPO/PPOIndicator.js",[e["Core/Series/SeriesRegistry.js"],e["Core/Utilities.js"]],function(t,e){var o,r=this&&this.__extends||(o=function(t,e){return(o=Object.setPrototypeOf||({__proto__:[]})instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw TypeError("Class extends value "+String(e)+" is not a constructor or null");function r(){this.constructor=t}o(t,e),t.prototype=null===e?Object.create(e):(r.prototype=e.prototype,new r)}),n=t.seriesTypes.ema,i=e.correctFloat,s=e.extend,a=e.merge,p=e.error,u=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return r(e,t),e.prototype.getValues=function(e,o){var r,n,s=o.periods,a=o.index,u=[],c=[],d=[];if(2!==s.length||s[1]<=s[0]){p('Error: "PPO requires two periods. Notice, first period should be lower than the second one."');return}var l=t.prototype.getValues.call(this,e,{index:a,period:s[0]}),f=t.prototype.getValues.call(this,e,{index:a,period:s[1]});if(l&&f){var h=s[1]-s[0];for(n=0;n<f.yData.length;n++)r=i((l.yData[n+h]-f.yData[n])/f.yData[n]*100),u.push([f.xData[n],r]),c.push(f.xData[n]),d.push(r);return{values:u,xData:c,yData:d}}},e.defaultOptions=a(n.defaultOptions,{params:{period:void 0,periods:[12,26]}}),e}(n);return s(u.prototype,{nameBase:"PPO",nameComponents:["periods"]}),t.registerSeriesType("ppo",u),u}),o(e,"masters/indicators/ppo.src.js",[e["Core/Globals.js"]],function(t){return t})});