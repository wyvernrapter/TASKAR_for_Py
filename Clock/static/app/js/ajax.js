function get_time() {
            // Ajax通信処理
            $.ajax({
                // リクエスト送信先URLの設定
                url: '{% url "record_app:i_ajax" %}',　　# ここで、i_ajaxViewを呼び出している。
                // 非同期通信フラグ（trueは非同期）
                async: true,
                // Ajax通信成功時にレスポンスデータ受け取り&処理実行
                success: function(data) {　　　　　　　　
                    document.getElementById("datetime_auto").innerHTML = data;
                }
            });
        }
        // 1秒ごとに実行する
        $(document).ready(function() {
            setInterval(get_time, 1000);
        });