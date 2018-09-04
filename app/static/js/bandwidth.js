$(function() {
    /* my add */
    var config0 = liquidFillGaugeDefaultSettings();
    config0.waveAnimateTime = 2000;
    /* my add */
    var gauge1 = loadLiquidFillGauge("fillgauge1", 55, config0);

    /* onclick refresh */
    function NewValue() {
        if (Math.random() > .5) {
            return Math.round(Math.random() * 100);
        } else {
            return (Math.random() * 100).toFixed(1);
        }
    }
})