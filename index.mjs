import fs from 'fs';
import child_process from 'child_process';
import path from 'path';

const directory = './images';
const directoryStyles = './styles';
let styleFiles = [];
fs.readdir(directoryStyles, (err, files) => {
	if (err) {
		console.error(`An error occurred while reading the directory: ${err}`);
		return;
	}
	styleFiles = files;
});
fs.readdir(directory, (err, files) => {
	if (err) {
		console.error(`An error occurred while reading the directory: ${err}`);
		return;
	}
	
	//const styleFiles = files.filter((file) => file.startsWith('style_'));
	
	files.forEach((file) => {
		const filePath = `${directory}/${file}`;
		const fileName = path.basename(filePath);
		const command = `style_transfer`;
		
		styleFiles.forEach(styleFile => {
			const styleName = path.basename(styleFile);
			const result = child_process.spawnSync(command, [filePath, styleFile, '-r', '512', '-o', `${fileName}_${styleName}.png`]);
			if (result.error) {
				console.error(`Error executing command: ${result.error}`);
				return;
			}
			if(result.stderr) {
				console.error(`Command error: ${result.stderr.toString()}`);
			}
			console.log(`Command output: ${result.stdout.toString()}`);
		});
		
	});
});