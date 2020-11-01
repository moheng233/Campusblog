// export var Codec:{
//     [keys: string]: {
//         "Encode": <D extends {}>(data:D) => string,
//         "Decode"?: <D>(data: string) => D
//     }
// } = {
//     "url": {
//         "Encode": <D extends {}>(data:D):string => {
//             return (new URLSearchParams(data)).toString();
//         },
//         "Decode": <D>(data:string):URLSearchParams => {
//             return (new URLSearchParams(data))
//         }
//     }
// };