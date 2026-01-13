var path = require('path');
const srcDir = "./src/UI/";

module.exports = {
    context: __dirname,
    entry: {
        // home:srcDir+"home.ts",
        // login:srcDir+"login.ts",
        // register:srcDir+"register.ts"
        main:"./test/main.tsx"
    },
    output: {
        path: path.join(__dirname, "/test_dist"),
        filename: '[name].js'
    },
    resolve: {
        extensions: [".tsx", ".ts", ".js"],
    },
    devtool:"source-map",
    module: {
        rules: [
            {
                test: /\.(ts|js)x$/,
                exclude: /node_modules/,
                use: [
                    {
                        loader: "babel-loader",
                        options: {
                            presets: [
                                "@babel/preset-env",
                                "@babel/preset-react",
                                "@babel/preset-typescript",
                            ],
                        },
                    },
                ],
            },
            {
                test: /\.ts$/,
                exclude: /node_modules/,
                use: { 
                    loader: "ts-loader"
                }
            },
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
            {
                test: /\.(png|jpe?g|gif|svg)$/i,
                type: "asset/resource",
            },
        ]
    }
}